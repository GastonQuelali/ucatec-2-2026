# UCatec 2 · 2026 — Material Didáctico de Informática

Repositorio con el material docente de la asignatura **Informática** de UCatec, organizado por módulos y unidades.

## Estructura del repositorio

```
modulo-1/
├── inf3/                     # Unidad 1 — Introducción a los Sistemas ERP
│   ├── 01_introduccion_erp.md    # Teoría completa de la unidad
│   ├── 02_presentacion_erp.md    # Slides (Marp)
│   ├── 03_guia_docente.md        # Guía y plan de clases
│   ├── erp_teoria_para_word.md   # Teoría lista para exportar a Word
│   ├── erp_teoria.docx           # Teoría en formato Word
│   ├── presentacion_erp.pptx     # Presentación en PowerPoint
│   ├── presentacion_erp.pdf      # Presentación en PDF
│   ├── assets/
│   │   ├── img/                  # Diagramas renderizados (PNG)
│   │   └── mermaid/              # Diagramas fuente (Mermaid)
│   └── pca/                      # Material del plan curricular anual
└── prog-avanzada/            # (en preparación)
```

## Módulo 1 · Unidad 1: Introducción a los Sistemas ERP

- **Objetivo:** que el estudiante comprenda qué es un ERP, su evolución, componentes y aplicaciones, y practique los conceptos en Odoo.
- **Recursos:**
  - `01_introduccion_erp.md` — teoría completa (definición, historia, arquitectura, módulos, tipos, multientidad, RBAC, práctica en Odoo).
  - `02_presentacion_erp.md` — presentación para clase (Marp + Mermaid).
  - `03_guia_docente.md` — guía docente con plan de 3 clases de 80 minutos.
- **Diagramas:** los fuentes `.mmd` están en `assets/mermaid/` y sus versiones renderizadas `.png` en `assets/img/`.

## Cómo renderizar la presentación

La presentación `02_presentacion_erp.md` usa **Marp**:

```bash
marp modulo-1/inf3/02_presentacion_erp.md --allow-local-files --pdf
```

Los diagramas Mermaid requieren `mmdc` (mermaid-cli) para regenerar los PNG:

```bash
mmdc -i assets/mermaid/01_evolucion_erp.mmd -o assets/img/01_evolucion_erp.png
```

## Autor

- **Ing. Gaston Genaro Quelali Calcina**

---

© 2026 · UCatec · Material de uso académico
