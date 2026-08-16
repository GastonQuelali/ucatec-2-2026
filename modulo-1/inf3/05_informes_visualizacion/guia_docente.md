# GUÍA DOCENTE — Tema 5: Informes, Visualización y Toma de Decisiones

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Sistemas de Datos para la Gestión · **Nivel:** Universitario
**Tiempo estimado:** 3 clases de 80 minutos (teoría + práctica + evaluación)
**Material de apoyo:** `teoria.md` (teoría) · `presentacion.md` (slides)

---

## 1. Objetivos de aprendizaje

Al finalizar el tema, el estudiante podrá:

1. **Explicar** qué es un informe y diferenciarlo de una consulta.
2. **Crear y personalizar** informes en Microsoft Access.
3. **Elegir** el tipo de gráfico adecuado según el objetivo.
4. **Definir** qué es un dashboard y un KPI con ejemplos.
5. **Construir** un dashboard básico en Power BI y en Google Looker Studio.
6. **Aplicar** el ciclo de decisión basada en datos a un caso real.

---

## 2. Plan de clases

### Clase 1 — Informes (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso Tema 4 + disparador: *"¿Cómo presentarían las ventas del mes a la gerencia?"* | Debate guiado |
| 20' | ¿Qué es un informe? Partes y tipos | Slides 3-7 |
| 30' | Crear y personalizar informes en Access | Slides 8-9 + demo |
| 15' | Ejercicio: informe "Ventas por Género" | Práctica asistida |
| 5' | Cierre | — |

### Clase 2 — Visualización y dashboards (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso | Preguntas orales |
| 20' | Visualización: gráficos según objetivo | Slides 10-12 |
| 20' | KPIs y anatomía de un dashboard | Slides 13-16 |
| 20' | Power BI: flujo de trabajo básico | Slide 17 + demo |
| 10' | Cierre | — |

### Clase 3 — Looker Studio + evaluación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso + comparativa Power BI vs Looker | Slides 18-19 |
| 25' | Looker Studio: crear dashboard desde Sheets | Slide 20 + demo |
| 25' | **Taller integrador** (evaluación) | Guía práctica |
| 10' | Cierre y dudas | — |

---

## 3. Taller práctico: Informes y dashboards (guía para el alumno)

### Parte 1 — Informe en Access

1. Crear la consulta "VentasPorGenero" que agrupe ventas por género.
2. **Asistente para informes** sobre esa consulta, agrupando por género.
3. Añadir un total general (`=Sum([Total])`) en el resumen.
4. Formatear moneda y agregar título y fecha. Guardar como "InformeVentas".

### Parte 2 — Dashboard en Power BI Desktop

1. Importar los datos desde Excel/CSV de la librería (o desde Access).
2. Crear 3 visuales:
   - **Tarjeta KPI:** ventas totales del mes.
   - **Barras:** ventas por género.
   - **Líneas:** evolución de ventas por mes.
3. Agregar un filtro de fecha. Guardar el archivo `.pbix`.

### Parte 3 — Dashboard en Looker Studio

1. Conectar una **Google Sheet** con datos de ventas.
2. Crear un gráfico de **barras** por género y un **scorecard** de total.
3. Agregar filtro de fecha y compartir con un vínculo.
4. Pegar el vínculo en un documento de entrega.

### Verificación final

| Verificación | Resultado esperado |
|---|---|
| Informe agrupado con total | Grupos + total general |
| Power BI muestra 3 visuales + filtro | Se filtra correctamente |
| Looker Studio comparte vínculo | Funciona sin instalar nada |
| El alumno explica los KPIs | Relaciona KPI con objetivo |

---

## 4. Actividades complementarias

**A. Investigación (tarea):** elegir un panel real de Power BI o Looker Studio (gallery/ejemplos) y describir: KPIs, gráficos usados y qué decisión permite tomar.

**B. Diseño en papel:** diseñar el dashboard "ideal" para una PYME a elección (indican KPIs, gráficos y filtros).

**C. Buenas prácticas:** investigar y listar 5 buenas prácticas de diseño de dashboards (con fuente).

---

## 5. Evaluación

### 5.1 Rúbrica para el taller integrador

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Informe en Access | Agrupado con totales | Funciona sin totales | No lo crea |
| Dashboard Power BI | 3 visuales + filtro | Visuales básicos | Incompleto |
| Dashboard Looker Studio | Comparte vínculo en vivo | Lo arma, no comparte | No lo arma |
| KPIs correctos | Relevantes y medibles | Aceptables | No definidos |
| Explica decisiones | Relaciona datos→decisión | Describe datos | Solo muestra números |

### 5.2 Cuestionario (12 preguntas de `teoria.md`)

1. ¿Informe vs consulta?
2. Partes de un informe.
3. Tipos de informes.
4. Pasos para crear un informe.
5. ¿Qué es la visualización de datos?
6. Gráficos según objetivo.
7. Comparación de herramientas.
8. ¿Qué es un dashboard?
9. ¿Qué es un KPI? Ejemplos.
10. Power BI vs Looker Studio.
11. Ciclo de decisión con datos.
12. Errores comunes de visualización.

---

## 6. Material de referencia

| Recurso | Uso |
|---|---|
| `teoria.md` | Texto de estudio completo |
| `presentacion.md` | Slides para dictar |
| `assets/img/*.png` | Diagramas exportados |
| Microsoft Access | Informes |
| Power BI Desktop | Dashboard |
| Google Looker Studio | Dashboard en la nube |
| BD `Gestion_Libreria.accdb` | Datos para talleres |

---

## 7. Sugerencias didácticas

- **Contexto gerencial:** enmarcar cada actividad con una decisión de negocio ("¿qué haría el gerente con esto?").
- **Dos herramientas:** mostrar el mismo dashboard en Power BI y Looker Studio para comparar en vivo.
- **KPI primero:** pedir que definan el KPI ANTES de armar el gráfico.
- **Errores a propósito:** mostrar un gráfico con escala engañosa para discutir ética de la visualización.
- **Cierre:** *"¿Qué KPI medirías para saber si la librería está sana?"*
