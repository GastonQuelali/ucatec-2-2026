# GUÍA DOCENTE — Unidad 1: Introducción a los Sistemas ERP

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Informática · **Nivel:** Universitario
**Tiempo estimado:** 3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `01_introduccion_erp.md` (teoría) · `02_presentacion_erp.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Definir** qué es un ERP y explicar sus cuatro ideas clave (integración, única base de datos, modularidad, procesos).
2. **Describir** la evolución histórica MRP → MRP II → ERP → ERP II → Cloud.
3. **Identificar** los componentes de un ERP (arquitectura de 3 capas y módulos típicos).
4. **Explicar** el flujo de datos integrado con un ejemplo (una venta).
5. **Clasificar** los ERP según despliegue, alcance y licencia; comparar productos líderes.
6. **Distinguir** autenticación de autorización, definir tenant, usuario, rol y permiso.
7. **Aplicar** los conceptos en Odoo: crear una empresa, crear usuarios y asignar roles.

---

## 2. Plan de clases

### Clase 1 — Fundamentos (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Introducción y disparador: *"¿Cómo se entera la contabilidad de lo que vendió el vendedor de la semana pasada?"* | Debate guiado |
| 30' | ¿Qué es un ERP, historia y objetivos | Slides 3-6 |
| 20' | Arquitectura de 3 capas y módulos | Slides 7-8 + diagramas |
| 15' | Flujo de datos integrado (caso venta) | Slide 9 |
| 5' | Cierre y repaso rápido | Preguntas orales |

### Clase 2 — Usos, tipos y selección (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso de la clase anterior | Preguntas orales |
| 20' | Usos por área y aplicaciones por sector | Slides 10-11 |
| 25' | Tipos de ERP y comparativa de productos | Slides 12-14 |
| 15' | Criterios de selección + caso: *"¿Qué ERP elegirías para una ferretería con 3 sucursales?"* | Slide 15 + trabajo en grupos |
| 10' | Puesta en común | — |

### Clase 3 — Inserción de usuarios y empresas + práctica Odoo (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Conceptos: tenant, usuario, rol, permiso, autenticación vs autorización | Slides 16-18 |
| 15' | RBAC y tabla de permisos por rol | Slide 19 |
| 40' | **Taller práctico en Odoo**: crear empresa, crear 3 usuarios, asignar roles, verificar accesos | Guía práctica (abajo) |
| 15' | Cierre, resolución de dudas y aviso de evaluación | — |

---

## 3. Taller práctico: Odoo paso a paso (guía para el alumno)

> **Preparación previa del docente:** crear una cuenta gratuita en https://www.odoo.com (o preparar una instalación local/Universidad Cloud). Verificar que la red del aula permite el acceso.

**Instrucciones para el alumno:**

1. **Ingresar a Odoo** con las credenciales provistas (o crear cuenta propia).
2. **Crear una empresa:**
   - Ajustes → General → Compañías → **Crear**
   - Cargar nombre ("Empresa Práctica SA"), país, moneda (ARS), dirección.
   - Guardar.
3. **Crear 3 usuarios** (Ajustes → Usuarios → Crear):
   - **Ana Pérez** — vendedora: nombre `ana@empresa.com`
   - **Juan Gómez** — contador: nombre `juan@empresa.com`
   - **Pedro Ruiz** — comprador: nombre `pedro@empresa.com`
4. **Asignar permisos por módulo** (pestaña "Permisos"):

| Módulo | Ana (vendedora) | Juan (contador) | Pedro (comprador) |
|---|---|---|---|
| Ventas | Operaciones propias | Solo lectura | Solo lectura |
| Inventario | Solo lectura | Solo lectura | Operaciones propias |
| Contabilidad | Sin acceso | Operaciones propias | Sin acceso |
| Ajustes | Sin acceso | Sin acceso | Sin acceso |

5. **Verificar accesos:** cerrar sesión e ingresar como cada usuario. Completar la tabla:

| Verificación | Ana | Juan | Pedro |
|---|---|---|---|
| ¿Puede entrar al sistema? | ✅ | ✅ | ✅ |
| ¿Puede cargar un pedido de venta? | ✅ | ❌ | ❌ |
| ¿Puede ver la contabilidad? | ❌ | ✅ | ❌ |
| ¿Puede crear una orden de compra? | ❌ | ❌ | ✅ |
| ¿Puede configurar la empresa? | ❌ | ❌ | ❌ |

6. **Reflexión escrita:** ¿por qué el vendedor no puede ver los costos internos? ¿Qué riesgo habría si todos tuvieran permisos de administrador?

**Resolución de problemas comunes:**

| Problema | Solución |
|---|---|
| No puedo crear usuarios | El usuario con el que entro no es administrador |
| No llega el correo de invitación | Asignar contraseña manualmente (Ajustes → Usuarios → Cambiar contraseña) |
| No aparece la empresa creada | Verificar en Ajustes → Compañías que se guardó correctamente |
| La interfaz está en inglés | Cambiar idioma en el perfil del usuario |

---

## 4. Actividades complementarias

**A. Trabajo en grupos — selección de ERP:** cada grupo recibe un perfil de empresa (pyme de retail, fábrica, clínica, estudio contable) y debe proponer un ERP justificando su elección con los criterios de la sección 1.2.6. Puesta en común al cierre.

**B. Investigación (tarea):** elegir un ERP vertical de una industria (salud, construcción, agro) y resumir sus módulos y casos de uso reales. Entrega: 1 página.

**C. Integración con la materia:** identificar en un ERP real dónde se guardan los datos (tablas de clientes, productos, ventas) y relacionarlo con las Unidades 2-6 (bases de datos, tablas, SQL). La capa de datos del ERP ES una base de datos relacional.

---

## 5. Evaluación

### 5.1 Rúbrica para el taller práctico (Odoo)

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Crea la empresa correctamente | Sin errores | Con ayuda | No completa |
| Crea y configura los 3 usuarios | Roles y permisos exactos | Roles parciales | Solo crea usuarios |
| Verifica accesos | Tabla completa y correcta | Tabla parcial | No verifica |
| Reflexión escrita | Vincula RBAC y seguridad | Describe sin análisis | No entrega |

### 5.2 Cuestionario (ver preguntas de repaso en `01_introduccion_erp.md`)

Preguntas sugeridas para la evaluación integradora:
1. Concepto y características de un ERP (sección 1.1 a 1.4).
2. Diferencia entre autenticación y autorización, con ejemplo.
3. Explicar el flujo de una venta en un ERP.
4. Clasificar un ERP dado (ej. "ERPNext instalado en un servidor propio para una fábrica" → open source, horizontal, on-premise).
5. Procedimiento completo de alta de un usuario con rol en Odoo.

### 5.3 Evaluación práctica (alternativa)

Entregar a cada alumno un perfil de rol (vendedor, contador, comprador) y un checklist de tareas permitidas y prohibidas. El alumno debe: crear el usuario con el rol correcto y demostrar el comportamiento esperado en Odoo.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `01_introduccion_erp.md` | Texto de estudio completo (teoría + diagramas + glosario) |
| `02_presentacion_erp.md` | Slides para dictar (Marp → PDF/PPTX) |
| `assets/img/*.png` | Diagramas exportados para Word/PDF/impresiones |
| Sitio oficial Odoo (https://www.odoo.com) | Práctica y documentación |
| Documentación ERPNext (https://docs.erpnext.com) | Alternativa open source |

---

## 7. Sugerencias didácticas

- **Contextualizar siempre:** partir de ejemplos de la vida cotidiana (ferretería, supermercado, empresa de software) antes de la teoría.
- **Usar la metáfora de la "única carpeta compartida"** para explicar la base de datos centralizada.
- **Vincular con el resto del programa:** recordar en cada clase que la Unidad 1 sirve de puente hacia bases de datos (Unidades 2-6): el ERP se construye sobre una BD.
- **Aprovechar el aula invertida:** pedir la lectura previa de las secciones 1.1-1.4 y dedicar la clase a ejercicios y casos.
- **Cerrar cada clase con 3 preguntas** de repaso oral para afianzar conceptos.
