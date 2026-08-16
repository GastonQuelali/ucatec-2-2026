---
marp: true
theme: default
paginate: true
header: "Tema 4 — Introducción al Lenguaje SQL y Automatización"
footer: "UCatec · Informática"
size: 16:9
style: |
  section { font-size: 26px; }
  section.title h1 { font-size: 58px; color: #0b4f8a; }
  section.title h2 { font-size: 30px; color: #555; }
  h2 { color: #0b4f8a; }
  table { font-size: 18px; }
  blockquote { background: #eef4fb; border-left: 5px solid #0b4f8a; padding: 8px 14px; }
  .columns { display: flex; gap: 30px; }
  .columns > div { flex: 1; }
  img { display: block; margin: 0 auto; }
  code { font-size: 18px; }
---

<!-- _class: title -->

# Introducción al Lenguaje SQL y Automatización
## Tema 4
#### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **¿Qué es SQL?** — definición y clasificación
2. **Importancia en la gestión empresarial**
3. **Estructura básica** — SELECT, INSERT, UPDATE, DELETE
4. **Consultas de extracción y manipulación**
5. **Formularios para captura de información** — Access, Google Forms, AppSheet

---

## ¿Qué es SQL?

> **SQL** = lenguaje estándar para comunicarse con bases de datos relacionales.

| Grupo | Qué hace | Comandos |
|---|---|---|
| **DDL** | Define la estructura | CREATE, ALTER, DROP |
| **DML** | Manipula los datos | SELECT, INSERT, UPDATE, DELETE |
| **DCL** | Controla permisos | GRANT, REVOKE |

> Este tema se centra en el **DML**, lo más usado en el trabajo diario.

---

## SQL: el puente entre la aplicación y la BD

<!-- fuente: assets/mermaid/01_puente_sql.mmd -->
![w:700](assets/img/01_puente_sql.png)

- Cajero registra venta → `INSERT INTO Ventas (...)`
- Gerente consulta el mes → `SELECT ... FROM Ventas WHERE ...`
- Cliente cambia dirección → `UPDATE Clientes SET ...`

> Access traduce lo que hacés en la cuadrícula a SQL automáticamente.

---

## Importancia en la gestión empresarial

| Necesidad | Cómo la resuelve SQL |
|---|---|
| Consultar al instante | `SELECT` sobre millones de registros |
| Mantener datos actualizados | `INSERT`, `UPDATE`, `DELETE` |
| Generar reportes | Consultas que alimentan informes |
| Tomar decisiones | Datos exactos y confiables |

---

## Interfaz visual vs SQL

<!-- fuente: assets/mermaid/02_interfaz_vs_sql.mmd -->
![w:360](assets/img/02_interfaz_vs_sql.png)

| Aspecto | Interfaz | SQL |
|---|---|---|
| Velocidad | Lenta en complejas | Directa |
| Reproducibilidad | Repetís clics | Se guarda y reutiliza |
| Documentación | Sin registro | La sentencia documenta |

---

## Los 4 comandos DML

<!-- fuente: assets/mermaid/03_comandos_dml.mmd -->
![w:600](assets/img/03_comandos_dml.png)

| Comando | Acción | ¿Riesgo sin WHERE? |
|---|---|---|
| `SELECT` | Leer | No |
| `INSERT` | Agregar | N/A |
| `UPDATE` | Modificar | Modifica todo |
| `DELETE` | Borrar | Borra todo |

---

## SELECT — leer datos

```sql
SELECT Titulo, Autor, Precio
FROM Libros
WHERE Precio > 50
ORDER BY Precio DESC;
```

| Cláusula | Función |
|---|---|
| `SELECT` | Campos a mostrar |
| `FROM` | Tabla origen |
| `WHERE` | Filtro |
| `ORDER BY` | Orden |

---

## INSERT — agregar datos

```sql
INSERT INTO Libros (Titulo, Autor, Genero, Precio, Stock)
VALUES ('Cien años de soledad',
        'Gabriel García Márquez', 'Novela', 120.00, 15);
```

> ⚠️ El orden de los `VALUES` debe coincidir con el de los campos.

---

## UPDATE — modificar datos

```sql
UPDATE Libros
SET Precio = Precio * 1.1
WHERE Genero = 'Historia';
```

> ⚠️ Sin `WHERE` se modifica **toda la tabla**.

---

## DELETE — eliminar datos

```sql
DELETE FROM Libros
WHERE Stock = 0;
```

> ⚠️ Sin `WHERE` se borra **toda la tabla** y **no se puede deshacer**.

---

## Anatomía de un SELECT

<!-- fuente: assets/mermaid/04_anatomia_select.mmd -->
![w:800](assets/img/04_anatomia_select.png)

El orden lógico de las cláusulas es fijo:

```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
```

---

## Seleccionar todo y alias

```sql
SELECT * FROM Libros;
```

```sql
SELECT Titulo, Precio * Stock AS ValorStock
FROM Libros;
```

| Titulo | ValorStock |
|---|---|
| Cien años de soledad | 1800.00 |
| El principito | 550.00 |

---

## Filtros con WHERE

| Operador | Ejemplo |
|---|---|
| `=` / `<>` | `Genero = 'Novela'` |
| `>` / `<` | `Precio > 50` |
| `BETWEEN` | `Precio BETWEEN 50 AND 100` |
| `LIKE` | `Titulo LIKE 'C*'` |
| `IN` | `Genero IN ('Novela','Historia')` |
| `AND` / `OR` | `Stock > 0 AND Precio < 100` |

---

## Manipulación en la práctica

**Actualizar con condición compuesta:**
```sql
UPDATE Libros
SET Stock = 0
WHERE Precio > 200 AND Genero = 'Técnico';
```

**Borrar hijo antes que padre:**
```sql
DELETE FROM Prestamos WHERE LibroID = 7;
DELETE FROM Libros WHERE ID = 7;
```

---

## ¿Qué es un formulario?

> Interfaz gráfica para **ingresar, modificar o consultar** datos de forma amigable.

**Ventajas:**
- Interfaz guiada
- Evita errores (valida tipos)
- Protege los datos
- Acelera la carga

---

## Flujo de captura de datos

<!-- fuente: assets/mermaid/05_flujo_captura.mmd -->
![w:700](assets/img/05_flujo_captura.png)

Formulario → Validación → SQL → Base de datos

> El formulario convierte la entrada del usuario en `INSERT` / `UPDATE`.

---

## Formularios en Access

- **Crear → Formulario** → vista Diseño
- **Partes:** encabezado, cuerpo (detalle), pie, campos calculados
- **Tipos:** simple, dividido, con subformulario, exploración

**Ejemplo:** formulario "Nuevo Préstamo" → lee el libro, pide socio y fecha → `INSERT INTO Prestamos`

---

## Otras herramientas de captura

<!-- fuente: assets/mermaid/06_herramientas_captura.mmd -->
![w:600](assets/img/06_herramientas_captura.png)

| Herramienta | Dónde van los datos | Ideal para |
|---|---|---|
| **Access** | BD local relacionada | Procesos formales |
| **Google Forms** | Google Sheets | Encuestas rápidas |
| **AppSheet** | Sheets/Cloud + app móvil | Trabajo de campo |

---

## Buenas prácticas de formularios

- Marcar campos obligatorios
- Usar listas desplegables
- Validar formatos (fechas, correos)
- Agrupar por secciones
- Probar la carga → verificar INSERT/UPDATE
- Conectar formulario a consultas filtradas

---

## Repaso rápido

1. ¿Qué es SQL y qué grupos tiene?
2. ¿Qué hacen SELECT, INSERT, UPDATE y DELETE?
3. ¿Qué riesgo hay sin `WHERE`?
4. Escribe un SELECT ordenado por precio descendente
5. Escribe un INSERT de un libro
6. ¿Qué es un formulario? ¿Qué ventajas tiene?
7. Compara Access, Google Forms y AppSheet
8. Menciona 3 buenas prácticas de formularios

---

<!-- _class: title -->
# ¡Gracias!
### Dudas y consultas
