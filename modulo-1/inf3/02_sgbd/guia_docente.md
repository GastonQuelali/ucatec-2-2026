# GUÍA DOCENTE — Tema 2: Manejo Básico de Sistemas de Gestión de Bases de Datos (SGBD)

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Definir** qué es un SGBD y explicar sus 4 funciones principales.
2. **Clasificar** los SGBD según su despliegue (escritorio, servidor, nube).
3. **Comparar** las herramientas SGBD (Access, MySQL, Google Tables, Airtable) y elegir la adecuada según el contexto.
4. **Crear, modificar y eliminar** tablas y registros en Microsoft Access.
5. **Seleccionar** el tipo de dato y las propiedades de campo adecuadas para cada situación.
6. **Aplicar** buenas prácticas de modelado, incluyendo normalización básica.

---

## 2. Plan de clases

### Clase 1 — Fundamentos y herramientas (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso Tema 1 + disparador: *"¿En qué se diferencia Access de Excel?"* | Debate guiado |
| 20' | ¿Qué es un SGBD? Funciones y ventajas | Slides 3-4 |
| 20' | Herramientas: Access, MySQL, Google Tables, Airtable | Slides 5-10 |
| 20' | Comparativa y árbol de decisión | Slides 11-12 |
| 10' | Cierre y repaso oral | Preguntas |

### Clase 2 — Tablas, registros, tipos de datos (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + práctica de apertura (abrir Access y ver interface) | PC + Access |
| 20' | Crear/modificar/eliminar tablas en Access | Slides 13-16 + demo |
| 20' | Trabajar con registros (insertar, editar, borrar, filtrar) | Slides 17-18 |
| 20' | Tipos de datos y propiedades de campo | Slides 19-21 |
| 10' | Ejercicio guiado: crear tabla "Libros" | Práctica asistida |

### Clase 3 — Práctica y evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso de conceptos clave | Preguntas orales |
| 40' | **Taller completo**: BD "Gestion_Libreria" + tabla Libros + registros + propiedades + tabla Prestamos | Guía práctica |
| 15' | Ejercicio individual de diseño (evaluación) | Rúbrica |
| 15' | Cierre, dudas y aviso de evaluación | — |

---

## 3. Taller práctico: Access paso a paso (guía para el alumno)

> **Preparación previa del docente:** verificar que Access esté instalado en todas las PC del aula. Si no hay licencia, usar la prueba gratuita de Microsoft 365 o el aula de informática de la universidad.

### Paso 1: Crear la base de datos

1. Abrir **Microsoft Access**.
2. Elegir **Base de datos en blanco**.
3. Nombrar: `Gestion_Libreria.accdb`. Guardar.

### Paso 2: Crear la tabla "Libros"

1. **Crear → Diseño de tabla**.
2. Definir campos:

| Campo | Tipo de dato | Propiedades |
|---|---|---|
| ID | Autonumérico | Clave principal |
| Titulo | Texto corto | Tamaño: 200 · Requerido: Sí |
| Autor | Texto corto | Tamaño: 100 · Requerido: Sí |
| Genero | Texto corto | Tamaño: 50 |
| Precio | Moneda | Regla: `>=0` |
| Stock | Número | Entero largo · Regla: `>=0` |
| Disponible | Sí/No | Valor predeterminado: Sí |

3. Guardar como **"Libros"**.

### Paso 3: Insertar registros

| ID | Titulo | Autor | Genero | Precio | Stock | Disponible |
|---|---|---|---|---|---|---|
| 1 | Cien años de soledad | Gabriel García Márquez | Novela | 89.00 | 10 | Sí |
| 2 | El principito | Antoine de Saint-Exupéry | Infantil | 55.00 | 15 | Sí |
| 3 | Historia de Bolivia | varios | Historia | 120.00 | 5 | Sí |

### Paso 4: Modificar y eliminar

1. Cambiar el precio del libro 2 a **60.00**.
2. Agregar el campo **"Editorial"** (Texto corto, 100).
3. Cargar la editorial de cada libro.
4. Eliminar el registro del libro 3 (prueba).

### Paso 5: Propiedades de campo

1. Verificar la regla de validación de "Stock" (`>=0`).
2. Probar ingresar un stock negativo → debe aparecer el error.
3. Probar ingresar un precio negativo → debe aparecer el error.

### Paso 6: Crear tabla "Prestamos" (puente al Tema 3)

| Campo | Tipo de dato | Propiedades |
|---|---|---|
| ID | Autonumérico | Clave principal |
| LibroID | Número | Entero largo · (será FK en Tema 3) |
| FechaPrestamo | Fecha/Hora | Formato: fecha corta |
| FechaDevolucion | Fecha/Hora | Formato: fecha corta |

Insertar 3 registros. **No crear la relación todavía** (se hará en el Tema 3).

### Verificación final

| Verificación | Resultado esperado |
|---|---|
| La tabla "Libros" existe con 7+1 campos | Sí |
| Los registros se cargaron y modificaron | Sí |
| La regla de validación funciona | Sí |
| La tabla "Prestamos" existe con 4 campos | Sí |

---

## 4. Actividades complementarias

**A. Investigación (tarea):** elegir MySQL, PostgreSQL o Airtable y resumir: qué es, ventajas, desventajas, un caso de uso real (1 página).

**B. Diseño de tabla:** diseñar la tabla "Clientes" para una tienda online: 8 campos con tipos de datos y propiedades justificados.

**C. Debate:** *"¿Access es suficiente para una empresa o siempre se necesita MySQL?"* — argumentar ambos lados.

---

## 5. Evaluación

### 5.1 Rúbrica para el taller práctico

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Crea la BD y tablas correctamente | Sin errores | Con ayuda | Incompleto |
| Define tipos de datos y propiedades | Correctos y justificados | Algunos correctos | Sin tipos |
| Inserta y modifica registros | Todos los pasos completos | Parcial | Solo inserta |
| Verifica validaciones | Las prueba y explica | Las prueba | No las verifica |
| Tabla Prestamos | Creada correctamente | Con ayuda | No la crea |

### 5.2 Cuestionario (12 preguntas de `teoria.md`)

1. ¿Qué es un SGBD y sus 4 funciones?
2. 3 tipos de SGBD con ejemplos.
3. Ventajas y limitaciones de Access.
4. Access vs MySQL: cuándo usar cada uno.
5. Vista Diseño vs Vista Hoja de datos.
6. Pasos para crear una tabla con clave primaria.
7. Tipos de datos de Access (mínimo 6).
8. ¿Cuándo un número es Texto?
9. 5 propiedades de campo.
10. ¿Qué es la clave primaria y por qué es obligatoria?
11. 4 buenas prácticas de modelado.
12. ¿Qué es la normalización? Ejemplo.

### 5.3 Evaluación práctica (alternativa)

Entregar a cada alumno el diseño de una tabla simple (ej. "Empleados") con campos, tipos y propiedades para implementar en Access en 20 minutos.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar |
| `assets/img/*.png` | Diagramas exportados |
| Microsoft Access | Herramienta de práctica |
| Microsoft Learn — Access | Documentación oficial |

---

## 7. Sugerencias didácticas

- **Comparar siempre con Excel:** el alumno ya conoce Excel; mostrar la misma tarea en Excel y en Access para evidenciar las diferencias.
- **Práctica desde la clase 1:** abrir Access aunque sea para explorar la interface.
- **Errores a propósito:** pedir ingresar datos inválidos para mostrar las validaciones funcionando.
- **Vincular con el Tema 3:** la tabla "Prestamos" que se crea acá será el punto de partida de las relaciones.
- **Cerrar con la pregunta:** *"¿Qué tipo de dato elegirías para el campo 'Carnet de identidad'? ¿Por qué?"*
