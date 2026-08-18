# UCatec 2 · 2026 — Material Didáctico de Informática

Repositorio con el material docente de UCatec, organizado por módulos y temas.

## Asignaturas

| Módulo | Asignatura | Descripción |
|---|---|---|
| `modulo-1/inf3/` | Sistemas de Datos para la Gestión (SIS216) | 7 temas: ERP, BDD, SGBD, SQL, informes y automatización |
| `modulo-1/prog-avanzada/` | Programación Avanzada (SIS120) | 10 unidades de POO, UML, colecciones, E/S, GUI, testing y tendencias (Java) |

A continuación, el detalle de cada asignatura.

---

## Sistemas de Datos para la Gestión (SIS216)

## Estructura del repositorio

```
modulo-1/inf3/
├── README.md
├── generate_word_md.py              # Script para generar teoria_para_word.md
├── generate_pptx.py                 # Script para generar presentacion.pptx/pdf
├── generate_pdf.py                  # Script para generar teoria.pdf (mmdc + marp)
├── foros.md                         # Temas de foro por tema (recomendados + opciones)
│
├── 00_introduccion_erp/             # Tema 0 — Introducción a los Sistemas ERP
│   ├── teoria.md                    # Teoría completa del tema
│   ├── presentacion.md              # Slides (Marp)
│   ├── guia_docente.md              # Guía docente y plan de clases
│   ├── teoria_para_word.md          # Generado: teoría con imágenes (para Word)
│   ├── teoria.docx                  # Teoría en Word
│   ├── teoria.pdf                   # Teoría en PDF
│   ├── presentacion.pptx            # Presentación en PowerPoint
│   ├── presentacion.pdf             # Presentación en PDF
│   └── assets/
│       ├── img/                     # Diagramas renderizados (PNG)
│       └── mermaid/                 # Diagramas fuente (Mermaid)
│
├── 01_bdd_relacionales/             # Tema 1 — Introducción y Práctica con BDD Relacionales
├── 02_sgbd/                         # Tema 2 — Manejo Básico de SGBD
├── 03_relaciones_consultas/         # Tema 3 — Relaciones, Consultas y Análisis
├── 04_sql_automatizacion/           # Tema 4 — Introducción al SQL y Automatización
├── 05_informes_visualizacion/       # Tema 5 — Informes, Visualización y Decisiones
├── 06_automatizacion_empresarial/   # Tema 6 — Automatización y Conectores Digitales
│
└── pca/                             # Material administrativo del PCA
    ├── contenido_minimo.md
    └── anterior.txt
```

## Convención de archivos por tema

| Archivo | Propósito |
|---|---|
| `teoria.md` | Contenido de estudio completo (fuente maestra) |
| `presentacion.md` | Slides para clase (Marp + Mermaid) |
| `guia_docente.md` | Plan de clases, evaluación y material didáctico |
| `teoria_para_word.md` | Generado por script (mermaid → imágenes) |
| `teoria.docx` | Exportado a Word |
| `teoria.pdf` | Generado por script (mmdc + Marp) |
| `presentacion.pptx` | Exportado a PowerPoint |
| `presentacion.pdf` | Exportado a PDF |
| `assets/mermaid/` | Diagramas fuente `.mmd` |
| `assets/img/` | Diagramas renderizados `.png` |

## Generar teoria_para_word.md

```bash
# Para un tema específico
python3 modulo-1/inf3/generate_word_md.py 00_introduccion_erp

# Para todos los temas
python3 modulo-1/inf3/generate_word_md.py --all

# Para todas las unidades de Programación Avanzada
python3 modulo-1/inf3/generate_word_md.py --base modulo-1/prog-avanzada --all
```

## Generar teoría en PDF

```bash
# Generar todos los teoria.pdf (inf3)
python3 modulo-1/inf3/generate_pdf.py --all

# Generar todos los teoria.pdf (prog-avanzada)
python3 modulo-1/inf3/generate_pdf.py --base modulo-1/prog-avanzada --all

# Un tema específico
python3 modulo-1/inf3/generate_pdf.py 00_introduccion_erp
```

Requiere [Mermaid CLI](https://mermaid.js.org/) y [Google Chrome](https://www.google.com/chrome/):

```bash
pip install markdown
npm install -g @mermaid-js/mermaid-cli
```

## Generar presentaciones (PPTX / PDF)

```bash
# Generar todas las presentaciones en PowerPoint
python3 modulo-1/inf3/generate_pptx.py --all

# También exportar PDF junto con PPTX
python3 modulo-1/inf3/generate_pptx.py --all --pdf

# Un tema específico
python3 modulo-1/inf3/generate_pptx.py 00_introduccion_erp

# Todas las unidades de Programación Avanzada
python3 modulo-1/inf3/generate_pptx.py --base modulo-1/prog-avanzada --all
```

Requiere [Marp CLI](https://marp.app/) instalado:

```bash
npm install -g @marp-team/marp-cli
```

También se puede usar Marp directamente:

```bash
marp modulo-1/inf3/00_introduccion_erp/presentacion.md --allow-local-files --pdf
```

Los diagramas Mermaid requieren `mmdc` (mermaid-cli):

```bash
mmdc -i assets/mermaid/01_evolucion_erp.mmd -o assets/img/01_evolucion_erp.png
```

## Contenidos del curso (SIS216)

| # | Tema | Estado |
|---|---|---|
| 0 | Introducción a los Sistemas ERP | ✅ Completo |
| 1 | Introducción y Práctica con BDD Relacionales | ✅ Completo |
| 2 | Manejo Básico de SGBD | ✅ Completo |
| 3 | Relaciones, Consultas y Análisis Avanzado | ✅ Completo |
| 4 | Introducción al SQL y Automatización | ✅ Completo |
| 5 | Informes, Visualización y Toma de Decisiones | ✅ Completo |
| 6 | Automatización Empresarial y Conectores Digitales | ✅ Completo |

---

## Programación Avanzada (SIS120)

Material completo en `modulo-1/prog-avanzada/` (10 unidades, lenguaje Java). Detalle de estructura, convención de archivos y generación de `teoria_para_word.md` en su [README](modulo-1/prog-avanzada/README.md).

| # | Unidad | Estado |
|---|---|---|
| 0 | Introducción a la POO | ✅ Completo |
| 1 | Clases y Objetos | ✅ Completo |
| 2 | UML y Diseño de Software | ✅ Completo |
| 3 | Herencia y Polimorfismo | ✅ Completo |
| 4 | Manejo de Excepciones | ✅ Completo |
| 5 | Genéricos y Colecciones | ✅ Completo |
| 6 | Entrada/Salida y Serialización | ✅ Completo |
| 7 | GUI y Manejo de Eventos | ✅ Completo |
| 8 | Testing y DevOps | ✅ Completo |
| 9 | Tendencias y Temas Emergentes | ✅ Completo |

## Autor

- **Ing. Gaston Genaro Quelali Calcina**

---

© 2026 · UCatec · Material de uso académico
