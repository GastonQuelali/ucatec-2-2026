# GUÍA DOCENTE — Tema 4: Introducción al Lenguaje SQL y Automatización

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Explicar** qué es SQL y su importancia en la gestión empresarial.
2. **Distinguir** DDL, DML y DCL, e identificar a qué grupo pertenece cada comando.
3. **Escribir** consultas SELECT, INSERT, UPDATE y DELETE correctas.
4. **Aplicar** filtros, orden, alias y condiciones en consultas.
5. **Diseñar** formularios de captura de datos en Access.
6. **Comparar** Access, Google Forms y AppSheet como herramientas de captura.

---

## 2. Plan de clases

### Clase 1 — Fundamentos de SQL (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso Tema 3 + disparador: *"¿Qué pasa cuando hacés clic en una consulta?"* | Debate guiado |
| 20' | ¿Qué es SQL? Clasificación (DDL/DML/DCL) | Slides 3-5 |
| 25' | SQL como puente BD-aplicación + importancia empresarial | Slides 6-7 |
| 15' | Interfaz visual vs SQL | Slide 8 |
| 10' | Cierre y dudas | — |

### Clase 2 — Comandos SQL (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso | Preguntas orales |
| 20' | SELECT y sus cláusulas | Slides 9-13 |
| 25' | INSERT, UPDATE, DELETE con ejemplos | Slides 14-17 |
| 15' | Ejercicios en pizarra + Access | Práctica asistida |
| 10' | Cierre | — |

### Clase 3 — Formularios + evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + advertencia de UPDATE/DELETE sin WHERE | — |
| 25' | Formularios en Access (crear y personalizar) | Slides 19-21 + demo |
| 20' | Google Forms y AppSheet (conceptos) | Slides 22-23 |
| 20' | **Taller integrador** (evaluación) | Guía práctica |
| 5' | Cierre | — |

---

## 3. Taller práctico: SQL y formularios (guía para el alumno)

> **Preparación previa del docente:** verificar que los alumnos tengan la BD `Gestion_Libreria.accdb` del Tema 2/3.

### Parte 1 — Consultas SQL en Access (Vista SQL)

Crear y guardar las siguientes consultas (en **Vista SQL** de Access):

1. **LibrosCaros:** título y precio de los libros con precio > 50, ordenado de mayor a menor.
2. **ValorStock:** título y `[Precio]*[Stock]` como `ValorStock`.
3. **BuscarGenero (parámetro):** `WHERE Genero = [Ingrese género]`.
4. **ResumenGenero:** `SELECT Genero, Count(ID), Avg(Precio) FROM Libros GROUP BY Genero;`

### Parte 2 — Manipulación (con respaldo)

1. **INSERT:** agregar 2 libros nuevos.
2. **UPDATE:** aumentar 10% los precios de "Novela".
3. **DELETE:** eliminar un libro de prueba sin stock.

Verificar cada cambio con un SELECT.

### Parte 3 — Formulario en Access

1. **Crear → Formulario** sobre la tabla Libros.
2. Personalizar en vista Diseño: título, secciones y un campo calculado.
3. Crear un formulario "Nuevo Préstamo" con subformulario.
4. Probar ingresar 3 préstamos desde el formulario y verificar con una consulta.

### Verificación final

| Verificación | Resultado esperado |
|---|---|
| Las 4 consultas se guardaron y ejecutan | Sin errores de sintaxis |
| Los INSERT/UPDATE/DELETE funcionaron | Datos verificables con SELECT |
| El formulario guarda préstamos | Aparecen en la tabla Prestamos |
| El SQL generado se puede leer | El alumno lo explica |

---

## 4. Actividades complementarias

**A. Investigación (tarea):** ¿qué es una inyección SQL y por qué es peligrosa? Escribir 5 líneas y un ejemplo de por qué nunca se debe concatenar datos de usuario sin validación (recursos: incibe.es).

**B. Diseño de formulario:** diseñar en papel un formulario de "Nuevo Cliente" indicando campos, obligatorios, tipos y listas desplegables.

**C. Comparativa:** completar una tabla comparativa Access vs Google Forms vs AppSheet (costo, dónde van los datos, dificultad, casos de uso).

---

## 5. Evaluación

### 5.1 Rúbrica para el taller integrador

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Consultas SELECT correctas | Las 4 sin errores | 2-3 correctas | Menos de 2 |
| Manipulación (I/U/D) | Las 3 correctas | 2 correctas | 1 o menos |
| Formulario funcional | Guarda y valida | Guarda datos | No funciona |
| Explica el SQL generado | Asocia SQL y resultados | Identifica comandos | No lo explica |
| Conoce riesgos (sin WHERE) | Lo explica con ejemplos | Lo menciona | No lo sabe |

### 5.2 Cuestionario (12 preguntas de `teoria.md`)

1. ¿Qué es SQL y por qué es estándar?
2. Grupos del lenguaje SQL.
3. Interfaz visual vs SQL.
4. SELECT con ORDER BY.
5. INSERT de un libro.
6. UPDATE de precios.
7. DELETE de sin stock.
8. Riesgo de UPDATE/DELETE sin WHERE.
9. ¿Qué es un formulario y sus ventajas?
10. Partes de un formulario en Access.
11. Comparativa de las 3 herramientas de captura.
12. 3 buenas prácticas de formularios.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar |
| `assets/img/*.png` | Diagramas exportados |
| Microsoft Access | Herramienta de práctica |
| BD `Gestion_Libreria.accdb` | BD reutilizada de Temas 2-3 |
| incibe.es | Seguridad (inyección SQL) |

---

## 7. Sugerencias didácticas

- **Vista SQL siempre:** mostrar el SQL generado por Access en cada consulta; reforzar que aprender SQL da control total.
- **Seguridad:** usar la inyección SQL como ejemplo de por qué la validación importa (conecta con el perfil de gestión).
- **Formularios:** el taller conecta directamente con el Tema 5 (informes) y 6 (automatización).
- **Errores a propósito:** intentar un UPDATE sin WHERE sobre una copia de la BD para demostrar el riesgo.
- **Cierre:** *"¿Qué pregunta de negocio responderías con un SELECT?"*
