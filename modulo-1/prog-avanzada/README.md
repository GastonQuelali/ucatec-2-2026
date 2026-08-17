# Programación Avanzada (SIS120) — Material Didáctico

Material docente de la asignatura **Programación Avanzada (SIS120)** de UCatec, organizado por unidades. El contenido se construye sobre el PCA (`pca/contenido_minimo.md`) y usa **Java** (JDK 17+, Maven, JUnit 5, JavaFX, GitHub Actions) como lenguaje principal.

## Estructura del repositorio

```
modulo-1/prog-avanzada/
├── README.md                       # Este documento
├── foros.md                        # Temas de foro por unidad (recomendados + opciones)
│
├── 00_introduccion_poo/            # Unidad 0 — Introducción a la POO
│   ├── teoria.md                   # Teoría completa de la unidad
│   ├── presentacion.md             # Slides (Marp)
│   ├── guia_docente.md             # Guía docente y plan de clases
│   ├── teoria_para_word.md         # Generado: teoría con imágenes (para Word)
│   └── assets/
│       ├── img/                    # Diagramas renderizados (PNG)
│       └── mermaid/                # Diagramas fuente (Mermaid)
│
├── 01_clases_objetos/              # Unidad 1 — Clases y Objetos
├── 02_uml_diseno/                  # Unidad 2 — UML y Diseño
├── 03_herencia_polimorfismo/       # Unidad 3 — Herencia y Polimorfismo
├── 04_excepciones/                 # Unidad 4 — Manejo de Excepciones
├── 05_genericos_colecciones/       # Unidad 5 — Genéricos y Colecciones
├── 06_io_serializacion/            # Unidad 6 — E/S y Serialización
├── 07_gui_eventos/                 # Unidad 7 — GUI y Manejo de Eventos
├── 08_testing_devops/              # Unidad 8 — Testing y DevOps
├── 09_tendencias/                  # Unidad 9 — Tendencias y Temas Emergentes
│
└── pca/                            # Material administrativo del PCA
    └── contenido_minimo.md
```

## Convención de archivos por unidad

| Archivo | Propósito |
|---|---|
| `teoria.md` | Contenido de estudio completo (fuente maestra) |
| `presentacion.md` | Slides para clase (Marp + Mermaid) |
| `guia_docente.md` | Plan de clases, evaluación y material didáctico |
| `teoria_para_word.md` | Generado por script (mermaid → imágenes) |
| `assets/mermaid/` | Diagramas fuente `.mmd` |
| `assets/img/` | Diagramas renderizados `.png` |

## Generar teoria_para_word.md

Se usa el script de inf3 extendido (soporta `--base`):

```bash
# Todas las unidades de prog-avanzada
python3 modulo-1/inf3/generate_word_md.py --base modulo-1/prog-avanzada --all

# Una unidad específica
python3 modulo-1/inf3/generate_word_md.py --base modulo-1/prog-avanzada 03_herencia_polimorfismo
```

## Contenidos del curso (SIS120)

| # | Unidad | Estado |
|---|---|---|
| 0 | Introducción a la Programación Orientada a Objetos | ✅ Completo |
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
