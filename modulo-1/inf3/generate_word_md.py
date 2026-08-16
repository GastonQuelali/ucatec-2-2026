#!/usr/bin/env python3
"""
Genera teoria_para_word.md a partir de teoria.md para cada tema.
Reemplaza bloques mermaid por referencias a imágenes PNG + leyenda.

Uso:
    python3 generate_word_md.py 00_introduccion_erp
    python3 generate_word_md.py --all
"""

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

# Mapeo de figuras por tema: cada lista se corresponde ordenadamente
# con los bloques mermaid que aparecen en teoria.md.
# Formato: (nombre_png, caption)
THEMES = {
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


def convert(source_text: str, figures: list) -> str:
    lines = source_text.split("\n")
    result = []
    figure_idx = 0
    in_mermaid = False
    skip_fig_caption = False

    for line in lines:
        stripped = line.strip()

        if stripped == "```mermaid" and not in_mermaid:
            in_mermaid = True
            continue

        if stripped == "```" and in_mermaid:
            in_mermaid = False
            if figure_idx < len(figures):
                img, caption = figures[figure_idx]
                result.append(f"![{caption}]({IMG_DIR}/{img})")
                result.append("")
                result.append(f"*Figura: {caption}*")
                result.append("")
                figure_idx += 1
                skip_fig_caption = True
            else:
                print(f"  Advertencia: bloque mermaid #{figure_idx + 1} "
                      f"sin mapeo de imagen", file=sys.stderr)
            continue

        if in_mermaid:
            continue

        if skip_fig_caption:
            if stripped == "":
                continue
            skip_fig_caption = False
            if stripped.startswith("*Figura") or stripped.startswith("_Figura"):
                continue

        result.append(line)

    if figure_idx < len(figures):
        print(f"  Advertencia: solo {figure_idx} bloques mermaid, "
              f"{len(figures)} figuras definidas", file=sys.stderr)

    return "\n".join(result)


def process_theme(theme_dir: Path) -> bool:
    theme_name = theme_dir.name
    source = theme_dir / "teoria.md"
    output = theme_dir / "teoria_para_word.md"

    if not source.exists():
        print(f"  Saltando {theme_name}: no existe teoria.md")
        return False

    figures = THEMES.get(theme_name)
    if figures is None:
        print(f"  Saltando {theme_name}: sin mapeo de figuras en THEMES")
        return False

    source_text = source.read_text(encoding="utf-8")
    output_text = convert(source_text, figures)
    output.write_text(output_text, encoding="utf-8")

    print(f"  OK: {theme_name}/teoria_para_word.md generado "
          f"({len(figures)} figuras)")
    return True


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 generate_word_md.py <tema> | --all",
              file=sys.stderr)
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "--all":
        themes = sorted(d for d in SCRIPT_DIR.iterdir()
                        if d.is_dir() and d.name[0:2].isdigit())
        if not themes:
            print("No se encontraron carpetas de temas", file=sys.stderr)
            sys.exit(1)
        print(f"Procesando {len(themes)} temas...")
        for theme_dir in themes:
            process_theme(theme_dir)
    else:
        theme_dir = SCRIPT_DIR / arg
        if not theme_dir.is_dir():
            print(f"Error: no se encontro la carpeta {arg}", file=sys.stderr)
            sys.exit(1)
        process_theme(theme_dir)


if __name__ == "__main__":
    main()
