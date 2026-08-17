# GUÍA DOCENTE — Unidad 3: Diseño Orientado a Objetos y UML

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Explicar** qué es UML y su utilidad en el diseño de software.
2. **Leer y construir** diagramas de clases, casos de uso y de secuencia.
3. **Transformar** un diagrama de clases a código Java.
4. **Identificar y aplicar** los patrones Singleton, Factory y Strategy.

---

## 2. Plan de clases

### Clase 1 — UML: estructura y funcionalidad (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Qué pasa si programamos sin planificar?"* | Debate guiado |
| 20' | UML + diagrama de clases | Slides 3-5 |
| 20' | Casos de uso y secuencia | Slides 6-8 |
| 25' | Del análisis al código (clase UML → Java) | Slides 9-10 |
| 5' | Cierre | — |

### Clase 2 — Patrones de diseño + práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | ¿Qué es un patrón de diseño? | Slide 11 |
| 30' | Singleton, Factory, Strategy con código | Slides 12-16 |
| 35' | **Taller**: modelar + implementar sistema de ventas | Guía práctica (abajo) |
| 5' | Cierre y aviso de evaluación | — |

---

## 3. Taller práctico (guía para el alumno)

1. **Modelar** (en papel o herramienta UML) un sistema de ventas:
   - `Cliente` (id, nombre) → realiza `Pedido`.
   - `Pedido` (fecha, total) → contiene `DetallePedido`.
   - `DetallePedido` (cantidad, precio) → referencia `Producto`.
   - `Producto` (id, nombre, precio).
2. **Transformar** el diagrama a clases Java (atributos privados, getters, constructores).
3. **Aplicar Factory**: crear una fábrica de productos de prueba.
4. **Aplicar Strategy**: un `Pedido` que puede notificar por email o SMS.

**Criterios de evaluación:**
- El diagrama de clases es correcto y completo.
- Las clases Java reflejan fielmente el diagrama.
- Los patrones se aplican de forma justificada.

---

## 4. Evaluación

- **Taller práctico (50%):** diagrama UML + implementación Java.
- **Evaluación formativa (20%):** preguntas orales.
- **Prueba escrita (30%):** lectura de diagramas UML y patrones.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_diagrama_clases.mmd` — diagrama de clases de la biblioteca.
- `assets/mermaid/02_casos_uso.mmd` — casos de uso de la biblioteca.
- `assets/mermaid/03_secuencia.mmd` — secuencia del préstamo.
- `assets/mermaid/04_analisis_a_codigo.mmd` — flujo análisis → código.
- `assets/mermaid/05_patron_singleton.mmd` — patrón Singleton.
- `assets/mermaid/06_patrones_factory_strategy.mmd` — Factory y Strategy.

---

## 6. Recursos complementarios

- Freeman, E. & Robson, E. *Head First Design Patterns* (O'Reilly).
- Gamma, E. et al. *Design Patterns* (GoF).
- Diagrams.net (draw.io) — herramienta UML gratuita.
- PlantUML / Mermaid — diagramas desde texto.
