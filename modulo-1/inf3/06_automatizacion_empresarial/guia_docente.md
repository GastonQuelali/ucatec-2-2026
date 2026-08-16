# GUÍA DOCENTE — Tema 6: Automatización Empresarial y Conectores Digitales

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 2-3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Explicar** qué es la automatización de procesos y cuándo conviene.
2. **Describir** los tres casos prácticos centrales (notificaciones, reportes, actualización de registros).
3. **Definir** conector, trigger, acciones y flujo de trabajo.
4. **Comparar** Zapier y Power Automate y elegir según el contexto.
5. **Diseñar** un flujo de trabajo digital en forma de diagrama.
6. **Aplicar** buenas prácticas y reconocer riesgos de la automatización.

---

## 2. Plan de clases

### Clase 1 — Fundamentos (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso Tema 5 + disparador: *"¿Qué tarea repetitiva hacés todos los días en la PC?"* | Debate guiado |
| 20' | ¿Qué es automatizar? Manual vs automatizado | Slides 3-6 |
| 30' | Los 3 casos prácticos con diagramas | Slides 7-12 |
| 15' | Ejercicio: identificar procesos automatizables en su entorno | Trabajo grupal |
| 5' | Cierre | — |

### Clase 2 — Conectores (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso | Preguntas orales |
| 20' | Conectores: trigger, pasos, acciones | Slides 13-15 |
| 20' | Zapier vs Power Automate | Slides 16-18 |
| 20' | Diseño de flujos: plantilla | Slides 19-21 + práctica |
| 10' | Cierre | — |

### Clase 3 — Taller + evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + buenas prácticas y riesgos | Slide 22 |
| 25' | Diseño de 3 flujos por equipos (diagramas) | Guía práctica |
| 25' | **Taller integrador** (evaluación) | Guía práctica |
| 10' | Cierre del tema y de la asignatura | Retroalimentación |

---

## 3. Taller práctico: Diseño de flujos de automatización (guía para el alumno)

> **Enfoque:** conceptual + casos prácticos (sin acceso requerido a Zapier/Power Automate). El alumno diseña flujos con diagramas y plantillas.

### Parte 1 — Identificar procesos automatizables

Enumerar 5 tareas repetitivas de su entorno (estudio, trabajo, hogar) y para cada una indicar:
- ¿Es repetitiva? ¿Es reglada? ¿Usa datos?

### Parte 2 — Diseñar 3 flujos con la plantilla

Usar la plantilla de diseño para estos 3 flujos:

**Flujo A — Notificación de factura vencida**
| Campo | Valor |
|---|---|
| Proceso | Aviso de facturas vencidas |
| Trigger | Fecha de vencimiento pasada y sin pago |
| Acciones | Enviar mail recordatorio al cliente |
| Condiciones | Monto > umbral |
| Frecuencia | Diario 9:00 |

**Flujo B — Reporte semanal de ventas**
| Campo | Valor |
|---|---|
| Proceso | Reporte de ventas semanal |
| Trigger | Lunes 8:00 |
| Acciones | Generar PDF y enviar a gerencia |
| Condiciones | Ninguna |
| Frecuencia | Semanal |

**Flujo C — Alta de cliente desde formulario**
| Campo | Valor |
|---|---|
| Proceso | Registro de clientes |
| Trigger | Nueva respuesta en formulario |
| Acciones | Crear registro en tabla Clientes + mail de bienvenida |
| Condiciones | Validar correo único |
| Frecuencia | Cada respuesta |

### Parte 3 — Diagrama

Para **uno** de los flujos, dibujar el diagrama (a mano o digital) con: trigger → pasos → acciones → fin.

### Verificación final

| Verificación | Resultado esperado |
|---|---|
| Identifica 5 procesos con criterios | Justifica cada criterio |
| Completa las 3 plantillas | Todos los campos coherentes |
| Diagrama correcto | Flujo claro de principio a fin |
| Explica riesgos | Menciona duplicados y errores |

---

## 4. Actividades complementarias

**A. Investigación (tarea):** investigar un ejemplo real de automatización en Zapier o Power Automate (plantilla oficial), resumir el flujo y sus apps.

**B. Debate:** "¿La automatización elimina puestos de trabajo o los transforma?" — argumentar con 3 ejemplos.

**C. Seguridad:** investigar qué permisos necesitan los conectores (scopes) y por qué es riesgoso otorgar permisos excesivos.

---

## 5. Evaluación

### 5.1 Rúbrica para el taller integrador

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Identifica procesos | 5 con criterios claros | 3-4 correctos | Menos de 3 |
| Plantillas completas | Las 3 coherentes | 2 correctas | 1 o menos |
| Diagrama del flujo | Claro y completo | Básico | Ausente |
| Conoce conectores | Explica trigger/acciones | Los menciona | No los distingue |
| Riesgos | Los explica con ejemplos | Los menciona | No los conoce |

### 5.2 Cuestionario (12 preguntas de `teoria.md`)

1. ¿Qué es la automatización y cuándo conviene?
2. Proceso manual vs automatizado.
3. Criterios de automatización.
4. Flujo de notificación de stock bajo.
5. Flujo de reporte semanal.
6. Flujo de actualización de registros.
7. ¿Qué es un conector? Componentes.
8. Ejemplo Forms → Sheets → Mail.
9. Comparativa Zapier vs Power Automate.
10. Criterios para elegir plataforma.
11. Pasos para diseñar un flujo.
12. Buenas prácticas + advertencia.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar |
| `assets/img/*.png` | Diagramas exportados |
| Zapier / Power Automate | Documentación y plantillas (opcional) |

---

## 7. Sugerencias didácticas

- **Cierre de asignatura:** conectar los 6 temas en un recorrido (datos → BD → consultas → SQL → informes → automatización).
- **Trabajo grupal:** cada equipo diseña un flujo para un área distinta (ventas, compras, RRHH).
- **Riesgo real:** mostrar que una automatización mal configurada puede duplicar registros (conecta con integridad del Tema 3).
- **Sin instalaciones:** el enfoque conceptual permite evaluar diseño sin requerir cuentas pagas.
- **Cierre final:** *"¿Qué proceso automatizarías primero en una PYME real y por qué?"*
