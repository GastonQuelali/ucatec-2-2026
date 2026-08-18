#!/usr/bin/env python3
"""
Genera teoria.pdf a partir de teoria_para_word.md usando markdown + Chrome headless.
Si faltan imágenes PNG renderizadas, las genera desde los .mmd con mmdc.

Requisitos:
    pip install markdown
    npm install -g @mermaid-js/mermaid-cli
    Google Chrome instalado

Uso:
    python3 generate_pdf.py --all
    python3 generate_pdf.py --base ../prog-avanzada --all
    python3 generate_pdf.py 00_introduccion_erp
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MMDC_BIN = "mmdc"
_mmdc_path = None

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

THEMES = {
    # --- Programación Avanzada (prog-avanzada) ---
    "00_introduccion_poo": [
        ("01_evolucion_paradigmas.png", "Evolución de los paradigmas de programación"),
        ("02_pilares_poo.png",           "Los cuatro pilares de la POO"),
        ("03_clase_vs_objeto.png",       "Clase como molde y objetos como instancias"),
        ("04_paradigmas_mixtos.png",     "Lenguajes modernos y paradigmas mixtos"),
    ],
    "01_clases_objetos": [
        ("01_anatomia_clase.png",        "Anatomía de una clase en UML"),
        ("02_modificadores_acceso.png",  "Modificadores de acceso en Java"),
        ("03_ciclo_vida_objeto.png",     "Ciclo de vida de un objeto"),
        ("04_gestion_dependencias.png",  "Gestión de dependencias con Maven y Gradle"),
    ],
    "02_uml_diseno": [
        ("01_diagrama_clases.png",       "Diagrama de clases de una biblioteca"),
        ("02_casos_uso.png",             "Diagrama de casos de uso de la biblioteca"),
        ("03_secuencia.png",             "Diagrama de secuencia del préstamo de libros"),
        ("04_analisis_a_codigo.png",     "Del análisis al código: flujo completo"),
        ("05_patron_singleton.png",      "Patrón Singleton: instancia única"),
        ("06_patrones_factory_strategy.png", "Patrones Factory y Strategy"),
    ],
    "03_herencia_polimorfismo": [
        ("01_relaciones_clases.png",     "Asociación, agregación, composición y herencia"),
        ("02_jerarquia_herencia.png",    "Jerarquía de herencia de Animal"),
        ("03_sobrecarga_sobreescritura.png", "Sobrecarga vs sobreescritura"),
        ("04_interface_vs_abstracta.png","Interface vs clase abstracta"),
        ("05_polimorfismo.png",          "Polimorfismo en acción con Figuras"),
        ("06_solid.png",                 "Los cinco principios SOLID"),
    ],
    "04_excepciones": [
        ("01_jerarquia_excepciones.png", "Jerarquía de excepciones en Java"),
        ("02_flujo_try_catch.png",       "Flujo de try/catch/finally"),
        ("03_ciclo_depuracion.png",      "Ciclo de depuración con logs y debugger"),
    ],
    "05_genericos_colecciones": [
        ("01_jerarquia_colecciones.png", "Jerarquía del framework de colecciones"),
        ("02_list_set_map.png",          "¿List, Set o Map? Decisión de estructura"),
        ("03_generics.png",              "Clase genérica Caja con T"),
        ("04_iteradores.png",            "Recorrido de colecciones con iterador"),
    ],
    "06_io_serializacion": [
        ("01_flujo_archivos.png",        "Flujo de lectura y escritura de archivos"),
        ("02_jerarquia_streams.png",     "Jerarquía de streams de bytes y caracteres"),
        ("03_serializacion.png",         "Ciclo de serialización y deserialización"),
        ("04_json_vs_xml.png",           "Comparativa JSON vs XML"),
    ],
    "07_gui_eventos": [
        ("01_arquitectura_gui.png",      "Arquitectura MVC de una aplicación GUI"),
        ("02_ciclo_eventos.png",         "Ciclo de manejo de eventos"),
        ("03_componentes_gui.png",       "Componentes típicos de una GUI"),
    ],
    "08_testing_devops": [
        ("01_flujo_testing.png",         "Flujo de pruebas unitarias y de integración"),
        ("02_git_workflow.png",          "Flujo de trabajo con Git y ramas"),
        ("03_pipeline_cicd.png",         "Pipeline de CI/CD"),
        ("04_junit.png",                 "Relación entre la clase y su test JUnit"),
        ("05_documentacion_estilo.png",  "Documentación, estilo y revisión de código"),
    ],
    "09_tendencias": [
        ("01_concurrencia_paralela.png", "Concurrencia vs paralelismo"),
        ("02_microservicios.png",        "Arquitectura de microservicios"),
        ("03_api_rest.png",              "Flujo de una API REST"),
        ("04_ciclo_tdd.png",             "Ciclo TDD: RED-GREEN-REFACTOR"),
        ("05_seguridad_etica.png",       "Desarrollo seguro y ético"),
    ],

    "00_introduccion_erp": [
        ("01_evolucion_erp.png",       "Evolución histórica de los ERP"),
        ("02_arquitectura_erp.png",    "Arquitectura en 3 capas de un ERP"),
        ("03_modulos_erp.png",         "Módulos típicos de un ERP en torno a la base de datos centralizada"),
        ("04_flujo_venta.png",         "Flujo de datos integrado: una venta"),
        ("09_ciclo_erp.png",           "Ciclo de vida de un ERP"),
        ("06_sectores_erp.png",        "Aplicaciones de los ERP por sector"),
        ("05_tipos_erp.png",           "Clasificación de los tipos de ERP"),
        ("11_seleccion_erp.png",       "Criterios de selección de un ERP"),
        ("07_multientidad.png",        "Estructura multientidad (multitenant)"),
        ("10_ciclo_usuario.png",       "Ciclo de vida de un usuario"),
        ("08_rbac.png",                "Modelo de seguridad RBAC"),
        ("12_crear_empresa.png",       "Paso 1 de la práctica en Odoo: crear una empresa"),
    ],
    "01_bdd_relacionales": [
        ("01_modelo_relacional.png", "Modelo relacional con tablas y relaciones"),
        ("02_estructura_tabla.png",  "Estructura de una tabla"),
        ("03_tipos_relaciones.png",  "Tipos de relaciones entre tablas"),
        ("04_migrar_excel.png",      "¿Cuándo migrar de Excel a un SGBD?"),
        ("05_clasificacion_sgbd.png","Clasificación de los SGBD"),
    ],
    "02_sgbd": [
        ("01_clasificacion_sgbd.png", "Clasificación de los SGBD según su despliegue"),
        ("02_cuando_usar.png",        "¿Qué herramienta SGBD elegir?"),
        ("03_vistas_tabla.png",       "Las dos vistas de una tabla en Access"),
        ("04_ciclo_tabla.png",        "Ciclo de vida de una tabla"),
        ("05_tipos_datos.png",        "Tipos de datos en Access"),
        ("06_checklist_modelado.png", "Checklist de buenas prácticas de modelado"),
        ("07_normalizacion.png",      "Normalización básica: eliminar datos repetidos"),
    ],
    "03_relaciones_consultas": [
        ("01_tipos_relaciones.png",   "Tipos de relaciones entre tablas"),
        ("02_tabla_intermedia.png",   "Relación N:M con tabla intermedia"),
        ("03_crear_relacion.png",     "Pasos para crear una relación en Access"),
        ("04_que_es_consulta.png",    "¿Qué es una consulta?"),
        ("05_tipo_consulta.png",      "Cómo elegir el tipo de consulta"),
    ],
    "04_sql_automatizacion": [
        ("01_puente_sql.png",         "SQL como puente entre la aplicación y la base de datos"),
        ("02_interfaz_vs_sql.png",    "Interfaz visual frente a SQL"),
        ("03_comandos_dml.png",       "Los cuatro comandos DML básicos"),
        ("04_anatomia_select.png",    "Anatomía de una sentencia SELECT"),
        ("05_flujo_captura.png",      "Flujo de captura de datos mediante formularios"),
        ("06_herramientas_captura.png","Herramientas de captura de datos"),
    ],
    "05_informes_visualizacion": [
        ("01_dato_a_decision.png",    "Del dato a la decisión"),
        ("02_partes_informe.png",     "Partes de un informe en Access"),
        ("03_que_es_visualizacion.png","La visualización convierte filas en lectura rápida"),
        ("04_anatomia_dashboard.png", "Anatomía de un dashboard"),
        ("05_flujo_powerbi.png",      "Flujo de trabajo básico en Power BI"),
        ("06_ciclo_decision.png",     "Ciclo de la decisión basada en datos"),
    ],
    "06_automatizacion_empresarial": [
        ("01_manual_vs_auto.png",     "Proceso manual frente a automatizado"),
        ("02_conviene_automatizar.png","Criterio para decidir si un proceso es automatizable"),
        ("03_caso_notificacion.png",  "Flujo de una notificación automática de stock bajo"),
        ("04_caso_reporte.png",       "Flujo de generación automática de reportes"),
        ("05_caso_actualizacion.png", "Flujo de actualización automática de registros"),
        ("06_como_funciona.png",      "Estructura de una automatización con conectores"),
        ("07_elegir_plataforma.png",  "Criterios para elegir entre Zapier y Power Automate"),
        ("08_pasos_flujo.png",        "Pasos para diseñar un flujo de trabajo"),
    ],
}

IMG_DIR = "assets/img"
MERMAID_DIR = "assets/mermaid"

CSS = """
@page { size: A4; margin: 20mm; }
body {
    font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
    font-size: 13px;
    line-height: 1.5;
    color: #333;
    max-width: 100%;
}
h1 { color: #0b4f8a; font-size: 22px; border-bottom: 2px solid #0b4f8a; padding-bottom: 6px; }
h2 { color: #0b4f8a; font-size: 18px; margin-top: 20px; }
h3 { color: #333; font-size: 15px; }
h4 { color: #555; font-size: 13px; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 12px; }
th, td { border: 1px solid #ccc; padding: 5px 8px; text-align: left; }
th { background: #eef4fb; font-weight: bold; }
blockquote {
    background: #eef4fb;
    border-left: 4px solid #0b4f8a;
    padding: 8px 12px;
    margin: 10px 0;
    font-style: italic;
}
img { max-width: 100%; display: block; margin: 10px auto; }
code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-size: 12px; }
pre { background: #f4f4f4; padding: 12px; border-radius: 4px; overflow-x: auto; }
pre code { background: none; padding: 0; }
hr { border: none; border-top: 1px solid #ddd; margin: 16px 0; }
"""


def _find_chrome():
    for path in CHROME_PATHS:
        if Path(path).exists():
            return path
    chrome = shutil.which("chrome") or shutil.which("google-chrome")
    if chrome:
        return chrome
    return None


def _check_tools():
    global _mmdc_path
    chrome = _find_chrome()
    if chrome is None:
        print("Error: Google Chrome no encontrado.\n"
              "Instalar desde: https://www.google.com/chrome/",
              file=sys.stderr)
        sys.exit(1)
    _mmdc_path = shutil.which(MMDC_BIN)
    if _mmdc_path is None:
        print("Error: mermaid-cli (mmdc) no encontrado en PATH.\n"
              "Instalar con:  npm install -g @mermaid-js/mermaid-cli",
              file=sys.stderr)
        sys.exit(1)


def _ensure_images(theme_dir: Path, figures: list) -> int:
    img_dir = theme_dir / IMG_DIR
    mmd_dir = theme_dir / MERMAID_DIR
    rendered = 0

    for png_name, _caption in figures:
        png_path = img_dir / png_name
        if png_path.exists():
            continue

        mmd_name = png_name.replace(".png", ".mmd")
        mmd_path = mmd_dir / mmd_name
        if not mmd_path.exists():
            print(f"    Advertencia: {mmd_name} no existe, saltando imagen",
                  file=sys.stderr)
            continue

        img_dir.mkdir(parents=True, exist_ok=True)
        cmd = [_mmdc_path, "-i", str(mmd_path), "-o", str(png_path),
               "-b", "transparent"]
        result = subprocess.run(cmd, capture_output=True, text=True,
                               cwd=str(theme_dir))
        if result.returncode != 0:
            print(f"    ERROR mmdc ({mmd_name}): {result.stderr.strip()}",
                  file=sys.stderr)
            continue
        rendered += 1

    return rendered


def _generate_pdf(theme_dir: Path) -> bool:
    import markdown

    source = theme_dir / "teoria_para_word.md"
    output = theme_dir / "teoria.pdf"

    md_text = source.read_text(encoding="utf-8")
    md_text = re.sub(r'(\*\*Contenido:\*\*)\n(- \[)', r'\1\n\n\2', md_text)
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    html_full = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        f"<style>{CSS}</style>"
        "</head><body>"
        f"{html_body}"
        "</body></html>"
    )

    tmp_html = Path(tempfile.gettempdir()) / f"teoria_{theme_dir.name}.html"
    tmp_html.write_text(html_full, encoding="utf-8")

    chrome = _find_chrome()
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        "--allow-file-access-from-files",
        f"--print-to-pdf={output}",
        "--no-pdf-header-footer",
        str(tmp_html),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

    tmp_html.unlink(missing_ok=True)

    if result.returncode != 0:
        print(f"    ERROR chrome: {result.stderr.strip()}", file=sys.stderr)
        return False

    if not output.exists():
        print(f"    ERROR: chrome no generó {output.name}", file=sys.stderr)
        return False

    size_kb = output.stat().st_size // 1024
    print(f"  OK: {output.name} ({size_kb} KB)")
    return True


def process_theme(theme_dir: Path) -> bool:
    theme_name = theme_dir.name
    source = theme_dir / "teoria_para_word.md"

    if not source.exists():
        print(f"  Saltando {theme_name}: no existe teoria_para_word.md")
        return False

    figures = THEMES.get(theme_name)
    if figures is None:
        print(f"  Saltando {theme_name}: sin mapeo de figuras en THEMES")
        return False

    n = _ensure_images(theme_dir, figures)
    if n > 0:
        print(f"  {n} imágenes renderizadas desde mermaid")

    return _generate_pdf(theme_dir)


def main():
    base_dir = SCRIPT_DIR
    args = sys.argv[1:]

    if len(args) >= 2 and args[0] == "--base":
        base_dir = Path(args[1]).resolve()
        args = args[2:]

    if len(args) < 1:
        print("Uso: python3 generate_pdf.py [--base DIR] <tema> | --all",
              file=sys.stderr)
        sys.exit(1)

    _check_tools()

    arg = args[0]

    if arg == "--all":
        themes = sorted(d for d in base_dir.iterdir()
                        if d.is_dir() and d.name[0:2].isdigit())
        if not themes:
            print("No se encontraron carpetas de temas", file=sys.stderr)
            sys.exit(1)
        print(f"Procesando {len(themes)} temas...")
    else:
        theme_dir = (base_dir / arg).resolve()
        if not theme_dir.is_dir():
            print(f"Error: no se encontro la carpeta {arg}", file=sys.stderr)
            sys.exit(1)
        themes = [theme_dir]

    ok = 0
    fail = 0
    for theme_dir in themes:
        print(f"\n{theme_dir.name}:")
        if process_theme(theme_dir):
            ok += 1
        else:
            fail += 1

    print(f"\nListo: {ok} generadas, {fail} errores")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
