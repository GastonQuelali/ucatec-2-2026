---
marp: true
theme: default
paginate: true
header: "Tema 2 — Manejo Básico de SGBD"
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
---

<!-- _class: title -->

# Manejo Básico de SGBD
## Sistemas de Gestión de Bases de Datos
### Tema 2
#### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **¿Qué es un SGBD?** — definición y funciones
2. **Herramientas SGBD** — Access, MySQL, Google Tables, Airtable
3. **Crear, modificar y eliminar tablas**
4. **Trabajar con registros**
5. **Tipos de datos y propiedades de campo**
6. **Buenas prácticas de modelado**
7. **Práctica en Access**

---

## ¿Qué es un SGBD?

> **SGBD** = Sistema de Gestión de Bases de Datos (DBMS)
> Software que permite **crear, administrar y manipular** bases de datos.

| Función | Qué hace |
|---|---|
| **Definir** | Crear tablas, campos y tipos de datos |
| **Manipular** | Insertar, modificar, eliminar, consultar |
| **Controlar** | Seguridad, integridad, concurrencia |
| **Almacenar** | Guardar datos de forma persistente |

---

## ¿Por qué no alcanza con Excel?

| Limitación | Consecuencia |
|---|---|
| Sin tipos de datos estrictos | Datos incorrectos ("abc" en precio) |
| Sin integridad referencial | Pedidos sin cliente válido |
| Sin concurrencia | Se pisan los cambios |
| Límite de filas | Se vuelve lento |
| Sin seguridad | Cualquiera ve todo |
| Sin SQL | Consultas complejas imposibles |

---

## Clasificación de SGBD

<!-- fuente: assets/mermaid/01_clasificacion_sgbd.mmd -->
![w:560](assets/img/01_clasificacion_sgbd.png)

| Tipo | Ejemplos | Ideal para |
|---|---|---|
| **Escritorio** | Access, SQLite | Aprendizaje, PYMEs |
| **Servidor** | MySQL, PostgreSQL | Empresas, web |
| **Nube** | Google Tables, Airtable | Equipos remotos |

---

## Microsoft Access — la principal

**Componentes de Access:**
- **Tablas** — almacenan los datos
- **Consultas** — extraen y procesan datos
- **Formularios** — pantallas para ingresar datos
- **Informes** — documentos imprimibles

**Ventajas:** visual, integrado con Office, ideal para aprender
**Limitaciones:** solo Windows, ~2 GB, pocos usuarios simultáneos

---

## MySQL

- SGBD de **servidor open source** más popular del mundo
- Usado en Facebook, YouTube, WordPress
- **Ventajas:** gratuito, rápido, estándar SQL
- **Desventajas:** requiere servidor, mayor curva de aprendizaje

---

## Google Tables y Airtable

| | Google Tables | Airtable |
|---|---|---|
| Tipo | Nube | Nube |
| Plan gratis | 10K filas | 1K filas |
| Ventajas | Colaboración real | Muy visual, no-code |
| Ideal para | Equipos Google | Prototipos rápidos |

---

## Comparativa de herramientas

| Criterio | **Access** | **MySQL** | **Google Tables** | **Airtable** |
|---|---|---|---|---|
| Tipo | Escritorio | Servidor | Nube | Nube |
| Costo | Licencia | Gratuito | Freemium | Freemium |
| SQL | Parcial | Completo | Parcial | No |
| Multiusuario | Limitado | Completo | Completo | Completo |
| Relaciones | Visuales | SQL | Simples | Simples |
| **Mejor para** | **Educación** | Web | Equipos | Prototipos |

> **En esta materia: Access**

---

## ¿Qué herramienta elegir?

<!-- fuente: assets/mermaid/02_cuando_usar.mmd -->
![w:520](assets/img/02_cuando_usar.png)

- **Remoto + escalable** → MySQL
- **Remoto + simple** → Nube (Tables/Airtable)
- **Aprender / PYME** → Access

---

## Las dos vistas de una tabla

<!-- fuente: assets/mermaid/03_vistas_tabla.mmd -->
![w:640](assets/img/03_vistas_tabla.png)

| Vista | Para qué sirve |
|---|---|
| **Hoja de datos** | Ver y editar registros (como Excel) |
| **Diseño** | Definir campos, tipos y propiedades |

---

## Crear una tabla (paso a paso)

1. **Crear → Diseño de tabla**
2. Definir campos (nombre + tipo de dato)
3. Seleccionar el campo ID → **Clave principal**
4. Configurar propiedades (tamaño, validación, requerido)
5. **Guardar** con nombre descriptivo

| Campo | Tipo | Propiedad |
|---|---|---|
| ID | Autonumérico | Clave principal |
| Nombre | Texto corto | Requerido: Sí |
| Precio | Moneda | Regla: >= 0 |

---

## Ciclo de vida de una tabla

<!-- fuente: assets/mermaid/04_ciclo_tabla.mmd -->
![w:900](assets/img/04_ciclo_tabla.png)

Diseñar → Crear → Insertar datos → Modificar → Consultar → Eliminar/Archivar

> ⚠️ Eliminar una tabla **borra todos sus datos** permanentemente

---

## Trabajar con registros

| Operación | Cómo |
|---|---|
| **Insertar** | Vista Hoja de datos → primera fila vacía |
| **Modificar** | Clic en la celda → editar |
| **Eliminar** | Seleccionar fila → Supr → Confirmar |
| **Buscar** | Ctrl + B |
| **Filtrar** | Clic derecho → Selección igual a... |

> ⚠️ La eliminación **no se puede deshacer**

---

## Tipos de datos en Access

<!-- fuente: assets/mermaid/05_tipos_datos.mmd -->
![w:580](assets/img/05_tipos_datos.png)

| Tipo | Ejemplo | Uso |
|---|---|---|
| Texto corto | Nombres | Texto hasta 255 |
| Texto largo | Descripciones | Párrafos |
| Número | Stock | Para calcular |
| Moneda | Precios | Valores $ |
| Autonumérico | IDs | Clave primaria |
| Fecha/Hora | Fecha pedido | Calendario |
| Sí/No | ¿Activo? | Lógico |

---

## El tipo de dato correcto

| Situación | Tipo correcto | Tipo incorrecto |
|---|---|---|
| Nombre | Texto corto | Número |
| Precio | Moneda | Texto |
| Teléfono "70012345" | **Texto** | Número (pierde el 0) |
| Stock | Número | Texto |
| Fecha | Fecha/Hora | Texto |
| ¿Pagado? | Sí/No | Texto |
| ID de cliente | Autonumérico | Texto libre |

> 💡 **Regla:** si un número **no se calcula**, es **Texto**

---

## Propiedades de campo

| Propiedad | Controla | Ejemplo |
|---|---|---|
| Tamaño del campo | Máx. caracteres | 50 |
| Formato | Cómo se muestra | Moneda |
| Máscara de entrada | Plantilla de ingreso | Teléfono |
| Valor predeterminado | Valor automático | "La Paz" |
| Regla de validación | Condición | `>=0` |
| Texto de validación | Mensaje de error | "No puede ser negativo" |
| Requerido | Obligatorio | Sí |

---

## La clave primaria

Reglas: **única**, **no nula**, **estable**

| Opción | Ejemplo |
|---|---|
| **Autonumérico** ✅ | 1, 2, 3... (recomendado) |
| Campo natural | DNI, RUC |
| Compuesta | (Pedido + Producto) |

---

## Buenas prácticas de modelado

<!-- fuente: assets/mermaid/06_checklist_modelado.mmd -->
![w:260](assets/img/06_checklist_modelado.png)

1. Nombre claro y singular
2. ID autonumérico como PK
3. Un dato por campo
4. Tipo de dato correcto
5. Sin datos repetidos
6. Definir propiedades
7. Pensar en el futuro
8. Definir relaciones (Tema 3)

---

## Normalización básica

<!-- fuente: assets/mermaid/07_normalizacion.mmd -->
![w:560](assets/img/07_normalizacion.png)

**1FN:** cada celda contiene un solo valor
**2FN:** un dato se almacena UNA vez, se referencia con claves

| ❌ Incorrecto | ✅ Correcto |
|---|---|
| Pedido 1 — Ana Pérez — La Paz | Clientes: ID 1 → Ana Pérez |
| Pedido 2 — Ana Pérez — La Paz | Pedido 1 → Cliente_ID 1 |

---

## Práctica en Access (resumen)

1. Crear BD `Gestion_Libreria.accdb`
2. Crear tabla **Libros** (7 campos: ID, Titulo, Autor, Genero, Precio, Stock, Disponible)
3. Insertar 3 libros
4. Modificar precio, agregar campo Editorial
5. Eliminar un registro
6. Verificar regla de validación (stock >= 0)
7. **Actividad:** crear tabla "Prestamos" (para Tema 3)

---

## Repaso rápido

1. ¿Qué es un SGBD y sus 4 funciones?
2. 3 tipos de SGBD según despliegue
3. Ventajas y limitaciones de Access
4. ¿Cómo se crea una tabla en Access?
5. ¿Cuándo un número es Texto?
6. ¿Qué es la clave primaria?
7. 3 buenas prácticas de modelado
8. ¿Qué es la normalización?

---

<!-- _class: title -->
# ¡Gracias!
### Dudas y consultas
