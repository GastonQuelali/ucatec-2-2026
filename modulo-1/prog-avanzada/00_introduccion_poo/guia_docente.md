# GUÍA DOCENTE — Unidad 1: Introducción a la Programación Orientada a Objetos

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Explicar** la evolución de la programación estructurada a la orientada a objetos.
2. **Definir** y ejemplificar los cuatro pilares de la POO (abstracción, encapsulamiento, herencia, polimorfismo).
3. **Distinguir** clase de objeto e instanciar objetos en Java.
4. **Reconocer** la aplicación de los mismos conceptos en Python y C#.
5. **Escribir** clases sencillas en Java con atributos, constructor y métodos.

---

## 2. Plan de clases

### Clase 1 — Fundamentos y pilares (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Por qué un programa grande se vuelve imposible de mantener?"* | Debate guiado |
| 20' | Evolución de paradigmas | Slides 3-4 |
| 25' | Los 4 pilares con ejemplos | Slides 5-9 |
| 20' | Clase vs objeto + primer código Java | Slides 10-11 |
| 5' | Cierre y preguntas orales | — |

### Clase 2 — Práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + ejemplos Java/Python/C# | Slides 12-14 |
| 30' | **Taller**: crear clase `Perro` y 3 instancias en Java | Guía práctica (abajo) |
| 30' | **Reto**: convertir el mismo código a Python | Comparación de sintaxis |
| 10' | Cierre y aviso de evaluación | — |

---

## 3. Taller práctico (guía para el alumno)

1. Crear un proyecto Java (IDEA, VS Code o consola con `javac`/`java`).
2. Definir la clase `Perro`:
   - Atributos privados: `nombre`, `raza`, `edad`.
   - Constructor con los tres atributos.
   - Método público `ladrar()` que imprima `"¡Guau!"`.
   - Método `mostrarDatos()`.
3. En `Main`, crear 3 perros y llamar a sus métodos.
4. **Reto extra:** reescribir la misma clase en Python y comparar sintaxis.

**Criterios de evaluación del taller:**
- Uso correcto de `private`, constructor y `this`.
- Creación y uso de instancias.
- Código legible con nombres descriptivos.

---

## 4. Evaluación

- **Taller práctico (40%):** clase `Perro` correcta y funcional.
- **Evaluación formativa (30%):** preguntas orales de repaso.
- **Participación (30%):** resolución del reto en Python.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_evolucion_paradigmas.mmd` — evolución de paradigmas.
- `assets/mermaid/02_pilares_poo.mmd` — los 4 pilares.
- `assets/mermaid/03_clase_vs_objeto.mmd` — clase y objetos.
- `assets/mermaid/04_paradigmas_mixtos.mmd` — lenguajes y paradigmas.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — "Object-Oriented Programming Concepts".
- Deitel & Deitel. *Java: How to Program* (cap. 1-2).
- W3Schools / GeeksforGeeks: *OOP Concepts*.
