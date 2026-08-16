# GUÍA DOCENTE — Tema 3: Relaciones, Consultas y Análisis Avanzado

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 4 clases de 80 minutos (relaciones + consultas + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Definir** los tres tipos de relaciones (1:1, 1:N, N:M) y cómo se implementan.
2. **Crear, editar y eliminar** relaciones en Access con integridad referencial.
3. **Explicar** la integridad referencial y los tipos de combinación.
4. **Crear** consultas de selección simples y con varias tablas.
5. **Aplicar** consultas de parámetros, totales y referencias cruzadas.
6. **Utilizar** consultas de acción (actualización, eliminación, creación de tabla, datos anexados).

---

## 2. Plan de clases

### Clase 1 — Relaciones (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso Tema 2 + disparador: *"¿Cómo conectamos 'Libros' con 'Prestamos'?"* | Debate guiado |
| 25' | Los 3 tipos de relaciones + tabla intermedia | Slides 3-5 |
| 25' | Crear relación en Access con integridad referencial | Slides 6-8 + demo |
| 15' | Tipos de combinación | Slide 9 |
| 5' | Cierre | — |

### Clase 2 — Consultas de selección (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + práctica de relación | PC + Access |
| 20' | ¿Qué es una consulta? Vista Diseño y SQL | Slides 10-12 |
| 25' | Consultas con criterios (filtros) | Slides 13-14 |
| 15' | Consultas con varias tablas | Slide 15 |
| 10' | Ejercicio guiado | Práctica asistida |

### Clase 3 — Consultas avanzadas (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso | Preguntas orales |
| 20' | Consultas de parámetros | Slide 16 |
| 25' | Consultas de totales (Sum, Avg, Count) | Slides 17-18 |
| 15' | Referencias cruzadas | Slide 19 |
| 10' | Ejercicio: totales y cálculos | Práctica asistida |

### Clase 4 — Consultas de acción + evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + advertencia de riesgo de consultas de acción | — |
| 30' | Los 4 tipos de consultas de acción | Slides 20-24 + demo |
| 25' | **Taller integrador** (evaluación) | Guía práctica |
| 15' | Cierre y dudas | — |

---

## 3. Taller práctico: Consultas y relaciones (guía para el alumno)

> **Preparación previa del docente:** verificar que los alumnos tengan la BD `Gestion_Libreria.accdb` del Tema 2 (con tablas "Libros" y "Prestamos" ya creadas).

### Parte 1 — Crear la relación

1. **Herramientas de base de datos → Relaciones**.
2. Agregar "Libros" y "Prestamos".
3. Arrastrar `Libros.ID` → `Prestamos.LibroID`.
4. Activar **Exigir integridad referencial** + **Actualizar en cascada**.
5. Crear y guardar.

### Parte 2 — Consultas de selección

1. Crear consulta "LibrosDisponibles": mostrar Titulo, Autor, Stock donde Disponible = Sí, ordenado por Título.
2. Crear consulta "PrestamosLibros": combinar Libros y Prestamos para mostrar Titulo y FechaPrestamo.
3. Crear consulta "BuscarGenero" (de parámetros): pregunta el género y filtra.

### Parte 3 — Consultas de totales

1. Consulta "ResumenGenero": para cada género → Count de libros y Avg de precio.
2. Consulta "ValorStock": mostrar Titulo y el cálculo `[Precio]*[Stock]`.

### Parte 4 — Consultas de acción (con respaldo)

1. **Actualización:** aumentar 10% el precio de los libros de "Historia".
2. **Eliminación:** eliminar un libro sin stock (probar con un registro de prueba).
3. **Creación de tabla:** crear "HistorialPrestamos" con los préstamos de 2026.
4. **Datos anexados:** agregar a "PedidosReponer" los libros con stock < 5.

### Verificación final

| Verificación | Resultado esperado |
|---|---|
| La relación 1:N se creó correctamente | Línea con 1 y ∞ |
| La consulta "LibrosDisponibles" filtra | Solo libros con Disponible = Sí |
| La consulta de parámetros pide el género | Funciona con distintos valores |
| Las totales agrupan por género | Cantidad y promedio correctos |
| La actualización modificó "Historia" | Precios aumentados 10% |
| La tabla HistorialPrestamos se creó | Existe en el panel |

---

## 4. Actividades complementarias

**A. Investigación (tarea):** investigar los comandos SQL `INNER JOIN`, `LEFT JOIN` y `RIGHT JOIN`. Escribir un ejemplo de cada uno para la BD de la librería.

**B. Diseño de relaciones:** para un sistema de ventas (Clientes, Pedidos, Productos, DetallePedido), dibujar el diagrama de relaciones indicando tipo y claves.

**C. Referencias cruzadas:** diseñar una consulta de referencias cruzadas para "cantidad de préstamos por libro y por mes".

---

## 5. Evaluación

### 5.1 Rúbrica para el taller integrador

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Crea la relación con integridad referencial | Sin errores | Con ayuda | No la crea |
| Consultas de selección con filtros | 3 correctas | 2 correctas | 1 o menos |
| Consultas de totales | Agrupa y calcula bien | Agrupa pero mal el cálculo | No agrupa |
| Consultas de acción | Las 4 correctas | 2-3 correctas | Solo 1 |
| Explica el SQL generado | Asocia SQL y Diseño | Identifica comandos | No lo explica |

### 5.2 Cuestionario (12 preguntas de `teoria.md`)

1. Los 3 tipos de relaciones con ejemplos.
2. ¿Cómo se resuelve un N:M?
3. Pasos para crear una relación en Access.
4. ¿Qué es la integridad referencial?
5. Tipos de combinación.
6. ¿Qué es una consulta y sus ventajas?
7. Consulta de parámetros: cuándo usarla.
8. Funciones de agregación con ejemplos.
9. ¿Qué es una referencias cruzadas?
10. Los 4 tipos de consultas de acción.
11. Riesgos de las consultas de acción.
12. SQL de una consulta de actualización.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar |
| `assets/img/*.png` | Diagramas exportados |
| Microsoft Access | Herramienta de práctica |
| BD `Gestion_Libreria.accdb` | BD del Tema 2 reutilizada |

---

## 7. Sugerencias didácticas

- **Continuidad:** el taller usa la misma BD del Tema 2; pedir que la tengan lista.
- **Vincular con SQL:** mostrar SIEMPRE el SQL que Access genera en cada consulta; esto prepara el Tema 4.
- **Riesgo de acción:** antes de cada consulta de acción, mostrar el respaldo y la advertencia de "no se puede deshacer".
- **Errores a propósito:** intentar insertar un préstamo con un LibroID inexistente para mostrar la integridad referencial en acción.
- **Cierre:** *"¿Qué consulta harías para saber cuál es tu género de libro más prestado?"*
