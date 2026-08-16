# TEMA 6 — AUTOMATIZACIÓN EMPRESARIAL Y CONECTORES DIGITALES

**Autor:** Ing. Gaston Genaro Quelali Calcina

---

**Contenido:**
- [6. Introducción a la automatización de procesos](#6-introducción-a-la-automatización-de-procesos)
- [6.1 Casos prácticos de automatización](#61-casos-prácticos-de-automatización)
- [6.2 Conectores y flujos de trabajo](#62-conectores-y-flujos-de-trabajo)
- [6.3 Diseño de flujos de trabajo digital](#63-diseño-de-flujos-de-trabajo-digital)

---

## 6. Introducción a la automatización de procesos

### 6.0.1 Definición

La **automatización de procesos** consiste en **reemplazar tareas manuales y repetitivas por flujos automáticos** que se ejecutan sin intervención humana (o con mínima intervención). Cuando hablamos de automatización *empresarial con datos*, nos referimos a que los datos son los que **disparan y alimentan** esos flujos.

> **Definición funcional:** si una tarea se hace igual todos los días ("cuando pasa X, hacer Y"), puede automatizarse.

### 6.0.2 Proceso manual vs automatizado

![Proceso manual frente a automatizado](assets/img/01_manual_vs_auto.png)

*Figura: Proceso manual frente a automatizado*


| Aspecto | Manual | Automatizado |
|---|---|---|
| Tiempo | Minutos u horas | Segundos |
| Errores | Posibles (tipos, olvidos) | Mínimos |
| Costo | Horas de personal | Una vez configurado |
| Escalabilidad | Limitada | Ilimitada (con límites de plan) |
| Trazabilidad | Depende de la persona | Registro automático |

### 6.0.3 ¿Qué procesos conviene automatizar?

![Criterio para decidir si un proceso es automatizable](assets/img/02_conviene_automatizar.png)

*Figura: Criterio para decidir si un proceso es automatizable*


**Criterios de automatización:**
- 🔁 **Repetitivo:** se hace con la misma frecuencia y pasos.
- 📏 **Reglado:** sigue reglas claras (si esto → aquello).
- 📊 **Basado en datos:** usa datos de tablas, planillas o sistemas.
- ⚠️ **Error humano alto:** hay riesgo de equivocación al hacerlo a mano.

> 💡 **Clave:** automatizar procesos *repetitivos, reglados y con datos*. No tiene sentido automatizar tareas que requieren criterio o creatividad.

### 6.0.4 Beneficios para la empresa

| Beneficio | Detalle |
|---|---|
| Ahorro de tiempo | Se eliminan tareas manuales |
| Reducción de errores | Menos carga de datos duplicados |
| Respuesta inmediata | Notificaciones y acciones al instante |
| Visibilidad | Cada paso queda registrado |
| Enfoque en lo importante | Las personas dedican tiempo a decisiones |

---

## 6.1 Casos prácticos de automatización

### 6.1.1 Caso 1: Notificaciones automáticas

**Situación:** en la librería, cuando un libro baja de 5 unidades de stock, alguien debe avisar al encargado de compras.

**Proceso automático:**

![Flujo de una notificación automática de stock bajo](assets/img/03_caso_notificacion.png)

*Figura: Flujo de una notificación automática de stock bajo*


| Paso | Cómo se hace |
|---|---|
| 1. Disparador | Se detecta un registro con Stock < 5 |
| 2. Regla | Si stock < 5 → enviar aviso |
| 3. Acción | Enviar mail/SMS al encargado |
| 4. Registro | Queda el registro del aviso enviado |

**Otros ejemplos:** aviso de factura vencida, confirmación de pedido al cliente, alerta de pago recibido.

### 6.1.2 Caso 2: Generación automática de reportes

**Situación:** cada lunes la gerencia quiere el reporte de ventas de la semana.

**Proceso automático:**

![Flujo de generación automática de reportes](assets/img/04_caso_reporte.png)

*Figura: Flujo de generación automática de reportes*


| Paso | Cómo se hace |
|---|---|
| 1. Disparador | Cada lunes a las 8:00 |
| 2. Datos | Consulta de ventas de la semana |
| 3. Acción | Generar PDF/reporte |
| 4. Envío | Mandarlo por mail a la lista de gerencia |

**Otros ejemplos:** reporte de cobranzas diario, resumen de clientes nuevos mensual, informe de stock semanal.

### 6.1.3 Caso 3: Actualización automática de registros

**Situación:** cuando se recibe un pedido de un cliente, el stock debe bajar automáticamente y debe crearse el registro del pedido.

**Proceso automático:**

![Flujo de actualización automática de registros](assets/img/05_caso_actualizacion.png)

*Figura: Flujo de actualización automática de registros*


| Paso | Cómo se hace |
|---|---|
| 1. Disparador | Nuevo pedido ingresado |
| 2. Acción A | Crear registro en Pedidos |
| 3. Acción B | Restar cantidad en Productos |
| 4. Verificación | Stock y pedido consistentes |

**Otros ejemplos:** mover datos de Google Forms a la BD principal, actualizar el estado de una factura al pagarse, sincronizar contactos entre herramientas.

---

## 6.2 Conectores y flujos de trabajo

### 6.2.1 ¿Qué es un conector?

Un **conector** es un **puente entre dos aplicaciones** que permite que una acción en una app dispare una acción en otra. Las plataformas de automatización (Zapier, Power Automate) funcionan conectando apps mediante **desencadenadores** (triggers) y **acciones**.

> **Definición funcional:** el conector es el "traductor" que permite que un formulario le avise a una planilla, que una planilla le avise a un mail, etc.

### 6.2.2 Cómo funciona una automatización

![Estructura de una automatización con conectores](assets/img/06_como_funciona.png)

*Figura: Estructura de una automatización con conectores*


**Componentes de un flujo:**
1. **Trigger (desencadenador):** el evento que inicia el flujo (nueva fila, nuevo mail, horario).
2. **Pasos intermedios:** filtros, transformaciones, condiciones.
3. **Acciones:** lo que se ejecuta en otras apps (crear registro, enviar mail, actualizar celda).

### 6.2.3 Ejemplo clásico de conector

**"Google Forms → Google Sheets → Mail":**

| Paso | Acción |
|---|---|
| Trigger | Nueva respuesta en el formulario |
| Paso | Se agrega la fila a la hoja de cálculo |
| Acción | Se envía un mail de confirmación al encuestado |

> Este es el ejemplo clásico de "conectar" apps con cero código.

### 6.2.4 Principales plataformas

**Zapier:**

| Característica | Detalle |
|---|---|
| Concepto | "Zaps": trigger + acciones |
| Apps conectadas | Miles (Google, Mail, Slack, Airtable...) |
| Dificultad | Baja, muy visual |
| Plan gratuito | Zapier Free (zaps limitados) |
| Ideal para | PYMEs y personas sin programación |

**Power Automate (Microsoft):**

| Característica | Detalle |
|---|---|
| Concepto | Flujos desde plantillas o en blanco |
| Apps conectadas | Ecosistema Microsoft + muchas otras |
| Integración fuerte | Office 365, Teams, SharePoint, Access/Excel |
| Dificultad | Media (editor moderno) |
| Licencia | Planes de Microsoft 365 / Power Platform |
| Ideal para | Empresas con Microsoft |

![Criterios para elegir entre Zapier y Power Automate](assets/img/07_elegir_plataforma.png)

*Figura: Criterios para elegir entre Zapier y Power Automate*


### 6.2.5 Comparativa Zapier vs Power Automate

| Criterio | Zapier | Power Automate |
|---|---|---|
| Costo | Gratis + planes | Planes Microsoft |
| Ecosistema | App-agnóstico (miles) | Fuerte en Microsoft |
| Dificultad | Baja | Media |
| Plantillas | Muchas | Muchas |
| Soporte | Comunidad amplia | Soporte Microsoft |
| Ideal para | Cualquier equipo | Empresas Microsoft |

---

## 6.3 Diseño de flujos de trabajo digital

### 6.3.1 Pasos para diseñar un flujo

![Pasos para diseñar un flujo de trabajo](assets/img/08_pasos_flujo.png)

*Figura: Pasos para diseñar un flujo de trabajo*


### 6.3.2 Plantilla de diseño de flujo

| Campo | Qué definir | Ejemplo (librería) |
|---|---|---|
| **Proceso** | Qué se automatiza | Aviso de stock bajo |
| **Trigger** | Qué lo inicia | Stock < 5 en Libros |
| **Acciones** | Qué se ejecuta | Enviar mail al encargado |
| **Condiciones** | Reglas adicionales | Solo si el libro está activo |
| **Frecuencia** | Cuándo revisa | Cada vez que cambia el stock |
| **Destinatarios** | A quién | jefe@libreria.com |

### 6.3.3 Buenas prácticas de automatización

| Práctica | Por qué |
|---|---|
| Empezar simple | Un flujo a la vez, probado |
| Documentar el flujo | Se entiende y mantiene |
| Definir fallas | ¿Qué pasa si falla? (aviso al admin) |
| No automatizar todo | Mantener lo que requiere criterio |
| Monitorear | Revisar ejecuciones fallidas |

> ⚠️ **Advertencia:** automatizar mal puede duplicar registros, enviar avisos equivocados o corromper datos. Siempre **probar con datos de prueba** antes de activar en producción.

---

## Preguntas de repaso

1. ¿Qué es la automatización de procesos y cuándo conviene?
2. Compara un proceso manual con uno automatizado.
3. ¿Qué criterios definen si un proceso es automatizable?
4. Describe el flujo de una notificación automática de stock bajo.
5. Describe el flujo de generación automática de un reporte semanal.
6. Describe el flujo de actualización automática de registros al recibir un pedido.
7. ¿Qué es un conector y cuáles son sus componentes?
8. Da un ejemplo clásico de conector (Forms → Sheets → Mail).
9. Compara Zapier y Power Automate.
10. ¿Qué criterios usarías para elegir entre Zapier y Power Automate?
11. Lista los pasos para diseñar un flujo de trabajo digital.
12. Menciona 3 buenas prácticas de automatización y una advertencia.

---

## Glosario

| Término | Significado |
|---|---|
| **Acción** | Operación que se ejecuta en una aplicación (crear registro, enviar mail) |
| **Automatización** | Reemplazo de tareas manuales por flujos automáticos |
| **Conector** | Puente entre dos aplicaciones que permite disparar acciones |
| **Desencadenador (trigger)** | Evento que inicia un flujo automático |
| **Flujo de trabajo** | Secuencia de pasos conectados que se ejecutan automáticamente |
| **Power Automate** | Plataforma de automatización de Microsoft |
| **Zapier** | Plataforma de automatización que conecta miles de apps |
| **Zap** | Nombre que Zapier da a un flujo (trigger + acciones) |
| **Filtro** | Condición que decide si un paso se ejecuta o no |
| **Trazabilidad** | Capacidad de registrar y seguir cada paso de un proceso |
