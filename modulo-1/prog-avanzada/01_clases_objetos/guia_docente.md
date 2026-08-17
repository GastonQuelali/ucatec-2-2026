# GUÍA DOCENTE — Unidad 2: Clases, Objetos y Tipos de Datos

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Definir** la estructura de una clase (atributos, métodos, constructor).
2. **Instanciar** objetos con `new` y distinguir el alcance de variables (local, de instancia, de clase).
3. **Aplicar** modificadores de acceso correctamente.
4. **Diferenciar** sobrecarga y sobreescritura de métodos.
5. **Integrar** librerías externas mediante Maven.

---

## 2. Plan de clases

### Clase 1 — Clases, objetos y alcance (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Cómo modelarías una cuenta bancaria?"* | Debate guiado |
| 25' | Estructura de clase + código Java | Slides 3-5 |
| 20' | Instanciación, ciclo de vida y alcance | Slides 6-7 |
| 20' | Modificadores de acceso + constructores | Slides 8-10 |
| 5' | Cierre y preguntas | — |

### Clase 2 — Sobrecarga, dependencias y práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso y sobrecarga vs sobreescritura | Slides 11-12 |
| 20' | Maven y gestión de dependencias | Slides 13-15 |
| 40' | **Taller**: proyecto Maven con clase `Producto` | Guía práctica (abajo) |
| 10' | Cierre y aviso de evaluación | — |

---

## 3. Taller práctico (guía para el alumno)

1. Crear un proyecto **Maven** (`mvn archetype:generate` o desde el IDE).
2. Definir la clase `Producto`:
   - Atributos privados: `nombre`, `precio`, `stock`.
   - Constructor con los tres atributos.
   - Métodos `getPrecio()`, `setPrecio(double)` y `aplicarDescuento(double)`.
   - Sobrecargar `aplicarDescuento(double)` con versión que acepte porcentaje.
3. En `Main`, crear 3 productos, aplicar descuentos y mostrar resultados.
4. **Reto extra:** agregar la librería Jackson al `pom.xml` y serializar un producto a JSON (avance de la Unidad 6).

**Criterios de evaluación:**
- Uso correcto de `private`, `this`, constructor y sobrecarga.
- El proyecto compila y ejecuta con Maven.
- Código legible.

---

## 4. Evaluación

- **Taller práctico (40%):** clase `Producto` con sobrecarga funcional en Maven.
- **Evaluación formativa (30%):** preguntas orales.
- **Participación (30%):** reto de serialización.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_anatomia_clase.mmd` — anatomía de una clase (UML).
- `assets/mermaid/02_modificadores_acceso.mmd` — modificadores de acceso.
- `assets/mermaid/03_ciclo_vida_objeto.mmd` — ciclo de vida de un objeto.
- `assets/mermaid/04_gestion_dependencias.mmd` — Maven vs Gradle vs manual.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — *Classes and Objects*, *Controlling Access*.
- Maven — *Introduction to the POM* (maven.apache.org).
- Deitel & Deitel. *Java: How to Program* (cap. 3-4).
