# GUÍA DOCENTE — Unidad 8: Desarrollo de Interfaces Gráficas y Manejo de Eventos

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Explicar** los fundamentos de una GUI y el patrón MVC.
2. **Crear** aplicaciones JavaFX con componentes básicos (Button, Label, TextField, TableView).
3. **Manejar** eventos con lambdas y handlers.
4. **Aplicar** validación y feedback para una UX simple.

---

## 2. Plan de clases

### Clase 1 — Fundamentos y componentes (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Por qué las apps usan ventanas y no solo comandos?"* | Debate guiado |
| 20' | GUI y JavaFX, patrón MVC | Slides 3-5 |
| 25' | Componentes y primer programa | Slides 6-7 |
| 20' | Mini-ejercicio: crear ventana con 3 controles | — |
| 5' | Cierre | — |

### Clase 2 — Eventos y UX + práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Ciclo de eventos y handlers | Slides 8-9 |
| 15' | Validación y feedback | Slide 10 |
| 10' | Principios de UX | Slides 11-12 |
| 40' | **Taller**: formulario JavaFX completo | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. Crear una app JavaFX "Registro de Productos":
   - `TextField` para nombre, `TextField` para precio.
   - Botón "Agregar" que valida y agrega a una `TableView`.
   - Botón "Limpiar" que vacía los campos.
   - `Alert` de éxito/error con feedback.
2. Aplicar el patrón **MVC**: la clase `Producto` (Modelo) no debe importar JavaFX.
3. **Reto extra:** agregar botón "Eliminar" que borre el producto seleccionado de la tabla.

**Criterios de evaluación:**
- La app compila y ejecuta con JavaFX.
- Validación de campos con feedback al usuario.
- La lógica de negocio está separada de la UI (MVC).
- Manejo correcto de eventos.

---

## 4. Evaluación

- **Taller práctico (60%):** formulario JavaFX funcional con validación.
- **Evaluación formativa (20%):** preguntas orales.
- **Participación (20%):** mini-ejercicio en clase.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_arquitectura_gui.mmd` — arquitectura MVC.
- `assets/mermaid/02_ciclo_eventos.mmd` — ciclo de eventos.
- `assets/mermaid/03_componentes_gui.mmd` — componentes típicos.

---

## 6. Recursos complementarios

- Oracle — *JavaFX Documentation* (openjfx.io).
- Baeldung — *JavaFX Tutorial*.
- UX Fundamentals — Nielsen Norman Group (artículos de usabilidad).
