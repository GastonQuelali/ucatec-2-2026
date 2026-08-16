# UCatec 2 · 2026 — Material Didáctico de Informática

Repositorio con el material docente de la asignatura **Sistemas de Datos para la Gestión** (SIS216) de UCatec, organizado por módulos y temas.

## Estructura del repositorio

```
modulo-1/inf3/
├── README.md
├── generate_word_md.py              # Script para generar teoria_para_word.md
├── foros.md                         # Temas de foro por tema (recomendados + opciones)
│
├── 00_introduccion_erp/             # Tema 0 — Introducción a los Sistemas ERP
│   ├── teoria.md                    # Teoría completa del tema
│   ├── presentacion.md              # Slides (Marp)
│   ├── guia_docente.md              # Guía docente y plan de clases
│   ├── teoria_para_word.md          # Generado: teoría con imágenes (para Word)
│   ├── teoria.docx                  # Teoría en Word
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
```

## Renderizar presentaciones

La presentación `presentacion.md` usa **Marp**:

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

## Autor

- **Ing. Gaston Genaro Quelali Calcina**

---

© 2026 · UCatec · Material de uso académico
