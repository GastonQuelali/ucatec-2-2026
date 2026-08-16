# FOROS — SISTEMAS DE DATOS PARA LA GESTIÓN (SIS216)

**Autor:** Ing. Gaston Genaro Quelali Calcina

---

**Contenido:**
- [¿Cómo usar este documento?](#cómo-usar-este-documento)
- [Tema 0 — Foros: Introducción a los ERP](#tema-0--foros-introducción-a-los-erp)
- [Tema 1 — Foros: Bases de Datos Relacionales](#tema-1--foros-bases-de-datos-relacionales)
- [Tema 2 — Foros: Manejo Básico de SGBD](#tema-2--foros-manejo-básico-de-sgbd)
- [Tema 3 — Foros: Relaciones, Consultas y Análisis Avanzado](#tema-3--foros-relaciones-consultas-y-análisis-avanzado)
- [Tema 4 — Foros: SQL y Automatización](#tema-4--foros-sql-y-automatización)
- [Tema 5 — Foros: Informes, Visualización y Toma de Decisiones](#tema-5--foros-informes-visualización-y-toma-de-decisiones)
- [Tema 6 — Foros: Automatización Empresarial y Conectores](#tema-6--foros-automatización-empresarial-y-conectores)

---

## ¿Cómo usar este documento?

Cada tema del programa tiene **un foro recomendado** (con consigna completa y rúbrica) y **tres opciones alternativas** (con consigna breve) para que el docente elija según el perfil del grupo o la carrera.

**Reglas generales de participación (aplican a todos los foros):**

| Regla | Recomendación |
|---|---|
| Extensión | 150-250 palabras por participación |
| Interacción | Responder al menos a 1 compañero |
| Fuentes | Citar teoría de la materia u otras fuentes |
| Plazo | Ventana de 1 semana desde la apertura |
| Peso | Según el plan de evaluación continua |

---

## Tema 0 — Foros: Introducción a los ERP

### Foro recomendado: Implementación de un ERP en una PYME

**Objetivo de aprendizaje:** aplicar los criterios de selección, módulos y fases de implantación de un ERP (vistos en el Tema 0) a un caso empresarial concreto.

**Situación/contexto:** la gerencia de una PYME decidió implementar un ERP. Tu tarea es proponer el plan de implantación y justificarlo.

**Preguntas guía:**
1. ¿Qué perfil de empresa elegiste (retail, fábrica, clínica, estudio contable) y qué ERP propones?
2. ¿Qué módulos implementarías primero y por qué en ese orden?
3. ¿Qué etapas del ciclo de vida seguirías y qué riesgos anticipas?
4. ¿Qué beneficios y qué costos (dinero, tiempo, personas) consideras críticos?

**Consigna de participación:** describir el plan en 200 palabras, responder al menos a un compañero y comparar una decisión con la suya.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Justificación del ERP | Usa criterios de selección con datos | Menciona criterios sin profundizar | No justifica |
| Orden de módulos | Lógico y argumentado | Razonable | Sin argumento |
| Ciclo de vida y riesgos | Identifica etapas y riesgos reales | Enumera etapas | No los reconoce |
| Interacción | Responde y compara con un compañero | Responde | Solo publica su tema |

### Opciones adicionales

- **Opción 1 — Selección de ERP según el perfil de empresa:** cada estudiante recibe un perfil (PYME de retail, fábrica, clínica, estudio contable) y propone un ERP justificando la elección con los criterios de la sección 1.2.6 del Tema 0.
- **Opción 2 — Seguridad en ERP (RBAC):** ¿por qué el control de acceso por roles es crítico en un ERP? Comparte un caso real o hipotético de un error de permisos y su impacto.
- **Opción 3 — Integración de módulos:** describe un flujo de negocio (una venta, una contratación) que atraviese al menos 3 módulos del ERP y explica cómo la base de datos centralizada lo hace posible.

---

## Tema 1 — Foros: Bases de Datos Relacionales

### Foro recomendado: Excel vs SGBD: ¿hasta cuándo Excel es suficiente en una PYME?

**Objetivo de aprendizaje:** aplicar los criterios de migración (volumen, concurrencia, integridad, seguridad) para decidir cuándo una hoja de cálculo deja de ser suficiente.

**Situación/contexto:** una PYME gestiona sus clientes, productos y pedidos en Google Sheets. El dueño pregunta: *"¿cuándo tengo que pasar a un sistema de base de datos?"*.

**Preguntas guía:**
1. ¿Qué señales concretas indicarían que la hoja ya no alcanza?
2. ¿Qué riesgos corre la empresa si sigue con la hoja más allá del punto de migración?
3. ¿Qué datos de la hoja necesitarían validación, integridad referencial o seguridad que hoy no tienen?
4. ¿Cómo convencerías al dueño con un ejemplo real?

**Consigna de participación:** proponer al menos 3 señales de migración con su justificación, y comentar la propuesta de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Señales de migración | 3+ señales con base teórica | Señales válidas | Superficiales |
| Riesgos | Concretos y bien explicados | Mencionados | No identificados |
| Ejemplo de convencimiento | Realista y persuasivo | Aceptable | Ausente |
| Interacción | Comenta con aporte | Comenta brevemente | No comenta |

### Opciones adicionales

- **Opción 1 — Clave primaria: natural vs autonumérica:** debate sobre usar un dato real (RUC, CI, email) o un número generado como PK. Argumenta con ventajas, desventajas y un ejemplo.
- **Opción 2 — Redundancia en tu entorno:** busca un ejemplo real de datos duplicados (planilla, sistema, papeles) y explica las 3 consecuencias vistas (inconsistencia, espacio, lentitud).
- **Opción 3 — Simulación en hojas de cálculo:** comparte una planilla (Excel/Sheets) que simule dos tablas relacionadas usando validación de datos y BUSCARX/BUSCARV, explicando qué regla de estructura aplicaste.

---

## Tema 2 — Foros: Manejo Básico de SGBD

### Foro recomendado: ¿Access es suficiente para una empresa o siempre se necesita MySQL?

**Objetivo de aprendizaje:** comparar SGBD de escritorio vs de servidor y defender una postura con criterios técnicos y de contexto.

**Situación/contexto:** un responsable de sistemas sostiene que *"Access es suficiente para cualquier PYME"*. Otro afirma que *"toda empresa seria necesita MySQL"*.

**Preguntas guía:**
1. ¿En qué casos Access es realmente la mejor opción?
2. ¿En qué casos se vuelve insuficiente (volumen, usuarios, seguridad, web)?
3. ¿Qué significa "suficiente" y cómo depende del contexto de la empresa?
4. ¿Cuál sería tu recomendación intermedia (ej. Access + migración futura)?

**Consigna de participación:** defender UNA postura con al menos 2 argumentos sólidos y responder a alguien que defienda la postura contraria.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Argumentos | 2+ sólidos y técnicos | Válidos pero generales | Débiles |
| Contexto | Considera tipo/tamaño de empresa | Lo menciona | No lo considera |
| Postura contraria | La responde con fundamento | La reconoce | La ignora |
| Interacción | Debate constructivo | Responde | Solo publica |

### Opciones adicionales

- **Opción 1 — Tipo de dato para "Carnet de identidad":** justifica qué tipo de dato y propiedades usarías en Access (número, texto, tamaño, regla de validación) y por qué.
- **Opción 2 — Escritorio vs nube:** compara Access con Google Tables/Airtable para un equipo remoto: costos, concurrencia, seguridad y cuándo elegirías cada uno.
- **Opción 3 — Buenas prácticas de modelado:** elige una tabla mal diseñada (real o inventada) y propón cómo corregirla aplicando normalización básica y checklist del Tema 2.

---

## Tema 3 — Foros: Relaciones, Consultas y Análisis Avanzado

### Foro recomendado: Diseña una relación N:M real con tabla intermedia

**Objetivo de aprendizaje:** aplicar el diseño de relaciones muchos a muchos y justificar la tabla intermedia en un caso real.

**Situación/contexto:** un club deportivo quiere registrar *"socios inscritos en actividades"* (un socio puede estar en varias actividades y una actividad tiene varios socios).

**Preguntas guía:**
1. ¿Cuáles son las tres tablas necesarias y qué claves usa cada una?
2. ¿Qué información extra puede guardar la tabla intermedia (fecha de inscripción, estado, cuota)?
3. ¿Qué errores de integridad referencial se evitarían con la relación bien diseñada?
4. ¿Cómo se consultaría "cuántos socios hay en cada actividad"?

**Consigna de participación:** describir el modelo (tablas, PK/FK, relaciones) y comentar el modelo de un compañero buscando mejoras.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Modelo N:M | Tabla intermedia correcta y justificada | Correcta sin justificar | Modelo incorrecto |
| Claves (PK/FK) | Identificadas correctamente | Parcial | Confusas |
| Consulta asociada | Bien planteada | Aceptable | Ausente |
| Interacción | Sugiere mejoras | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Consulta de parámetros para un negocio:** diseña una consulta de parámetros útil para una empresa real (ej. "informe de ventas del cliente X") y explica qué criterio pide al usuario y qué devuelve.
- **Opción 2 — Riesgos de las consultas de acción:** ¿qué puede salir mal si alguien ejecuta un UPDATE o DELETE sin WHERE o sin respaldo? Narra un caso real o hipotético y cómo prevenirlo.
- **Opción 3 — Referencias cruzadas en acción:** propón un caso donde una consulta de referencias cruzadas (bidimensional) sea mejor que una tabla convencional y describe filas, columnas y valor.

---

## Tema 4 — Foros: SQL y Automatización

### Foro recomendado: ¿Qué pregunta de negocio responderías con un SELECT?

**Objetivo de aprendizaje:** formular preguntas de negocio y traducirlas a consultas SQL correctas.

**Situación/contexto:** la gerencia quiere respuestas a preguntas de negocio usando la base de datos de la empresa (ej. librería: ventas, stock, clientes).

**Preguntas guía:**
1. ¿Qué pregunta de negocio elegiste (ventas, stock, clientes, cobranzas)?
2. Escribe el SELECT completo (campos, FROM, WHERE, ORDER BY) que la responde.
3. ¿Qué filtro o condición fue lo más difícil de traducir y por qué?
4. ¿Qué decisión tomaría la gerencia con ese resultado?

**Consigna de participación:** publicar pregunta + SQL + decisión, y validar el SQL de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Pregunta de negocio | Relevante y específica | Válida | Trivial |
| SQL correcto | Sintaxis y lógica correctas | Parcialmente correcto | Incorrecto |
| Decisión asociada | Concreta y accionable | Aceptable | Ausente |
| Interacción | Valida y mejora SQL ajeno | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Inyección SQL:** investiga qué es la inyección SQL (recursos: incibe.es), explica por qué es peligrosa y cómo la validación de entrada la previene.
- **Opción 2 — Formularios: Access vs Google Forms vs AppSheet:** compara las tres herramientas de captura para un caso real (registro de pedidos en una PYME) y justifica cuál elegirías.
- **Opción 3 — El peligro de un UPDATE sin WHERE:** describe una situación real o hipotética donde un UPDATE/DELETE sin WHERE causó un desastre y qué controles evitarían repetirlo.

---

## Tema 5 — Foros: Informes, Visualización y Toma de Decisiones

### Foro recomendado: ¿Qué KPI medirías para saber si la librería está sana?

**Objetivo de aprendizaje:** definir KPIs relevantes y diseñar el dashboard que los visualiza para apoyar una decisión.

**Situación/contexto:** sos el encargado de la librería del curso y la gerencia quiere un dashboard con los indicadores clave de salud del negocio.

**Preguntas guía:**
1. ¿Qué 3 KPIs elegirías (ventas, stock, clientes, cobranza) y por qué son los más importantes?
2. ¿Qué gráfico usarías para cada uno y por qué (barras, líneas, tarjeta)?
3. ¿Qué decisión permitiría tomar cada KPI si se sale de rango?
4. ¿Con qué herramienta lo armarías: Power BI o Looker Studio? Justifica.

**Consigna de participación:** publicar los 3 KPIs con su gráfico y herramienta, y comentar las elecciones de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| KPIs | Relevantes, medibles, accionables | Válidos | Genéricos |
| Gráficos | Adecuados al objetivo | Aceptables | Mal elegidos |
| Decisiones | Concretas por KPI | Parciales | Ausentes |
| Herramienta | Justificada | Mencionada | Sin justificar |
| Interacción | Comenta con aporte | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Power BI vs Looker Studio para una PYME:** elige una herramienta para una PYME concreta y justifica con costo, fuentes de datos, compartición y curva de aprendizaje.
- **Opción 2 — Ética de la visualización:** analiza un gráfico engañoso (escala manipulada, datos recortados) y explica qué decisión equivocada podría provocar y cómo corregirlo.
- **Opción 3 — Diseño de un dashboard "ideal":** diseña en papel o digital el dashboard de un área a elección (ventas, RRHH, marketing) indicando KPIs, gráficos y filtros.

---

## Tema 6 — Foros: Automatización Empresarial y Conectores

### Foro recomendado: ¿La automatización elimina puestos de trabajo o los transforma?

**Objetivo de aprendizaje:** argumentar sobre el impacto laboral y organizacional de la automatización usando ejemplos del Tema 6.

**Situación/contexto:** un debate en la empresa: algunos temen que automatizar "deje gente sin trabajo"; otros sostienen que "libera a las personas para tareas de mayor valor".

**Preguntas guía:**
1. ¿Qué tareas concretas se automatizan y qué tareas quedan para las personas?
2. ¿Qué habilidades nuevas necesitan los trabajadores afectados?
3. ¿La automatización crea empleos (nuevos roles) o solo los elimina?
4. Argumenta tu postura con al menos 2 ejemplos reales o hipotéticos.

**Consigna de participación:** tomar una postura con argumentos y ejemplos, y responder a la postura contraria de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Postura | Clara y argumentada | Presente pero débil | Confusa |
| Ejemplos | 2+ concretos | Uno | Ausentes |
| Análisis de tareas | Diferencia tareas automatizables vs humanas | Parcial | No lo hace |
| Postura contraria | La responde con fundamento | La menciona | La ignora |

### Opciones adicionales

- **Opción 1 — Proceso a automatizar primero en una PYME:** elige un proceso real (notificaciones, reportes, actualización de registros), diseña su flujo (trigger → acciones → condiciones) y justifica por qué empezar por él.
- **Opción 2 — Zapier vs Power Automate:** para una empresa concreta (una con Microsoft, otra sin ella), justifica qué plataforma elegirías y por qué.
- **Opción 3 — Riesgos de los conectores:** investiga qué permisos (scopes) piden los conectores y qué puede pasar si se otorgan permisos excesivos o se configuran mal (duplicación, envíos erróneos).
