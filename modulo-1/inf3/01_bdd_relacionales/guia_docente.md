# GUÍA DOCENTE — Tema 1: Introducción a Bases de Datos Relacionales

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Definir** qué es una base de datos y sus componentes fundamentales (tablas, campos, registros, claves).
2. **Distinguir** entre clave primaria y clave foránea, y explicar su importancia.
3. **Identificar** los tres tipos de relaciones entre tablas (1:1, 1:N, N:M).
4. **Comparar** hojas de cálculo y SGBD, enumerando limitaciones y ventajas de cada uno.
5. **Clasificar** los SGBD en escritorio, servidor y nube, con ejemplos de cada tipo.
6. **Explicar** las funciones de un SGBD y el rol de SQL.

---

## 2. Plan de clases

### Clase 1 — Fundamentos de bases de datos (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Cómo gestionás los datos de una ferretería con 500 productos?"* | Debate guiado |
| 25' | ¿Qué es una BD? Definición, conceptos fundamentales | Slides 3-4 |
| 20' | Tablas, registros, claves (PK y FK) | Slides 5-6 + diagrama ER |
| 15' | Tipos de relaciones (1:1, 1:N, N:M) | Slide 7 |
| 10' | Cierre y preguntas de repaso | Preguntas orales |

### Clase 2 — Hojas de cálculo vs SGBD (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso de la clase anterior | Preguntas orales |
| 20' | Hojas de cálculo como BD: capacidades y limitaciones | Slides 8-9 |
| 25' | Comparativa completa Excel vs SGBD | Slide 10 + tabla |
| 15' | ¿Qué es un SGBD? Tipos y clasificación | Slides 11-13 |
| 10' | SQL: introducción al lenguaje | Slide 14 |

### Clase 3 — Práctica y evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso y conceptos clave | Preguntas orales |
| 35' | **Taller práctico**: crear una BD en Access, diseñar tablas, insertar datos | Guía práctica (abajo) |
| 20' | Ejercicio de diseño: *"Diseñá las tablas para una biblioteca escolar"* | Trabajo en grupos |
| 15' | Puesta en común, cierre y aviso de evaluación | — |

---

## 3. Taller práctico: Access paso a paso

### Paso 1: Crear una base de datos

1. Abrir Microsoft Access
2. Seleccionar **Base de datos en blanco**
3. Nombrar: `Ferreteria_Practica.accdb`
4. Guardar en la carpeta del alumno

### Paso 2: Crear tabla "Clientes"

1. **Crear → Tabla en diseño**
2. Definir campos:

| Campo | Tipo de dato | Propiedades |
|---|---|---|
| ID | Autonumérico | Clave primaria (automática) |
| Nombre | Texto corto (50) | Requerido: Sí |
| Email | Texto largo | — |
| Telefono | Texto corto (15) | — |
| Ciudad | Texto corto (30) | Valor predeterminado: "La Paz" |

3. Guardar como "Clientes"

### Paso 3: Crear tabla "Productos"

| Campo | Tipo de dato | Propiedades |
|---|---|---|
| ID | Autonumérico | Clave primaria |
| Nombre | Texto corto (100) | Requerido: Sí |
| Precio | Moneda | Valor predeterminado: 0 |
| Stock | Número entero largo | Regla de validación: >=0 |

### Paso 4: Insertar registros

1. Abrir tabla "Clientes" en **Vista Hoja de datos**
2. Insertar 5 clientes de ejemplo
3. Abrir tabla "Productos" e insertar 5 productos

### Paso 5: Modificar y eliminar

1. Cambiar el teléfono de un cliente
2. Eliminar un producto
3. Agregar un campo "Direccion" a la tabla Clientes

---

## 4. Actividades complementarias

**A. Diseño de BD (tarea):** diseñar las tablas necesarias para gestionar una **biblioteca escolar** (libros, socios, préstamos). Definir campos, tipos de datos y claves. Entrega: 1 página.

**B. Investigación:** elegir uno de estos SGBD (MySQL, PostgreSQL, Airtable) y resumir en 10 bullet points: qué es, para qué sirve, ventajas y desventajas.

**C. Comparación:** crear una tabla comparativa entre Excel y Access para un caso específico (ej. gestión de stock de una tienda).

---

## 5. Evaluación

### 5.1 Rúbrica para el taller práctico

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Crea la BD correctamente | Sin errores | Con ayuda | No completa |
| Diseña las tablas con campos y tipos adecuados | Todos los campos correctos | Algunos campos faltan | Sin tipos de datos |
| Inserta y modifica registros | 5+ registros, modificaciones correctas | 3 registros | Solo 1-2 registros |
| Identifica PK y FK | Explica correctamente | Identifica pero no explica | No identifica |

### 5.2 Cuestionario (10 preguntas de `teoria.md`)

1. Definición de base de datos y sus 5 ideas clave.
2. Diferencia entre campo, registro y tabla.
3. PK vs FK con ejemplo.
4. Los 3 tipos de relaciones.
5. 4 limitaciones de Excel como BD.
6. 4 señales para migrar a SGBD.
7. 4 funciones de un SGBD.
8. Clasificar SGBD en 3 tipos.
9. Qué es SQL y 3 comandos básicos.
10. Cuándo usar Access vs MySQL.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar (Marp → PDF/PPTX) |
| `assets/img/*.png` | Diagramas para Word/PDF/impresiones |
| Microsoft Access (instalado) | Práctica en clase |
| Microsoft Learn — Access | Documentación oficial |

---

## 7. Sugerencias didácticas

- **Partir de lo conocido:** empezar con Excel (que todos conocen) y mostrar sus limitaciones antes de presentar el SGBD.
- **Usar la metáfora de la biblioteca** para explicar la estructura de una BD.
- **Vincular con el Tema 0:** recordar que el ERP del Tema 0 usa una base de datos relacional debajo.
- **Práctica temprana:** que los alumnos abran Access desde la primera clase, aunque sea solo para ver la interface.
- **Cerrar con la pregunta:** *"Si tuvieras que gestionar los datos de una empresa, ¿usarías Excel o Access? ¿Por qué?"*
