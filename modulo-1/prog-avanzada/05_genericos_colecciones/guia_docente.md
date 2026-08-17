# GUÍA DOCENTE — Unidad 6: Genéricos, Colecciones y Estructuras Avanzadas

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Escribir** clases y métodos genéricos con seguridad de tipos.
2. **Elegir** la estructura de colección adecuada (List, Set, Map, Queue).
3. **Recorrer** colecciones con iteradores y for-each.
4. **Aplicar** Streams para manipulación funcional de datos.
5. **Justificar** la eficiencia de cada estructura.

---

## 2. Plan de clases

### Clase 1 — Genéricos y colecciones (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Qué pasaría si una lista guardara cualquier cosa?"* | Debate guiado |
| 20' | Genéricos: problema y solución | Slides 3-4 |
| 25' | Jerarquía de colecciones | Slides 5-7 |
| 20' | Ejemplos List/Set/Map/Queue | Slides 8-9 |
| 5' | Cierre | — |

### Clase 2 — Iteradores, Streams y práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Iteradores y for-each | Slides 10-11 |
| 20' | Streams: filter/map/sorted/limit | Slides 12-14 |
| 10' | Eficiencia y decisión de estructura | Slide 15 |
| 35' | **Taller**: catálogo con Map + Streams | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. Crear una clase `Producto` (id, nombre, precio, stock) con genéricos en las colecciones.
2. Construir un catálogo con `Map<String, Producto>` (id como clave).
3. Con Streams: filtrar productos agotados, ordenar por precio, calcular el más caro.
4. Usar `Iterator` para eliminar productos sin stock durante el recorrido.
5. **Reto extra:** comparar `ArrayList` vs `HashSet` midiendo tiempos de búsqueda con `System.nanoTime()`.

**Criterios de evaluación:**
- Uso correcto de genéricos (sin warnings de raw types).
- Elección justificada de estructuras.
- Streams aplicados correctamente.
- Lectura de tiempos para eficiencia.

---

## 4. Evaluación

- **Taller práctico (50%):** catálogo con colecciones y streams funcional.
- **Evaluación formativa (20%):** preguntas orales.
- **Prueba escrita (30%):** genéricos, colecciones, iteradores.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_jerarquia_colecciones.mmd` — jerarquía del framework.
- `assets/mermaid/02_list_set_map.mmd` — decisión List/Set/Map.
- `assets/mermaid/03_generics.mmd` — clase genérica Caja.
- `assets/mermaid/04_iteradores.mmd` — recorrido con iterador.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — *Generics*, *Collections Framework*, *Streams*.
- Baeldung — *Java Collections*, *The Stream API*.
- Deitel & Deitel. *Java: How to Program* (cap. 17).
