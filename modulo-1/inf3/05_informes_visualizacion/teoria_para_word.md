# TEMA 5 — INFORMES, VISUALIZACIÓN Y TOMA DE DECISIONES

**Autor:** Ing. Gaston Genaro Quelali Calcina

---

**Contenido:**
- [5. Informes: qué son y para qué sirven](#5-informes-qué-son-y-para-qué-sirven)
- [5.1 Creación y personalización de informes](#51-creación-y-personalización-de-informes)
- [5.2 Herramientas para visualización de datos](#52-herramientas-para-visualización-de-datos)
- [5.3 Dashboards básicos](#53-dashboards-básicos)
- [5.4 De los datos a las decisiones](#54-de-los-datos-a-las-decisiones)

---

## 5. Informes: qué son y para qué sirven

### 5.0.1 Definición

Un **informe** es una **presentación organizada de datos** extraídos de la base de datos, con formato y estructura pensados para la lectura y el análisis. A diferencia de una consulta (que devuelve datos crudos), el informe los **presenta** de forma clara: con títulos, agrupaciones, totales, fechas y gráficos.

> **Definición funcional:** si la consulta es "la pregunta", el informe es "la respuesta presentada en un documento ordenado y listo para compartir".

**¿Para qué sirven los informes?**
- 📄 Documentar ventas, inventarios, cobranzas.
- 📊 Resumir resultados para gerencia.
- 🧾 Emitir documentos formales (facturas, listados, constancias).
- 📈 Dar soporte a las decisiones con datos.

### 5.0.2 Del dato a la decisión

![Del dato a la decisión](assets/img/01_dato_a_decision.png)

*Figura: Del dato a la decisión*


| Etapa | Qué hace | Herramienta |
|---|---|---|
| Base de datos | Almacena los datos | Access, MySQL |
| Consulta | Extrae y procesa | SQL / Access |
| Informe | Presenta organizado | Access, Excel |
| Dashboard | Visualiza indicadores | Power BI, Looker Studio |
| Decisión | Acción informada | La persona |

---

## 5.1 Creación y personalización de informes

### 5.1.1 Partes de un informe en Access

![Partes de un informe en Access](assets/img/02_partes_informe.png)

*Figura: Partes de un informe en Access*


### 5.1.2 Tipos de informes en Access

| Tipo | Para qué |
|---|---|
| **Informe simple** | Listado de registros sin agrupar |
| **Informe con agrupaciones** | Totales parciales por grupo (por género, por mes) |
| **Informe con subinformes** | Datos maestro-detalle (cliente y sus pedidos) |
| **Informe con gráficos** | Visualización dentro del informe |
| **Etiquetas postales** | Impresión de etiquetas/etiquetas de dirección |

### 5.1.3 Crear un informe en Access

1. Seleccionar la **tabla o consulta** que alimenta el informe.
2. **Crear → Asistente para informes** (o "Informe" directo).
3. Elegir los **campos** a incluir.
4. Definir **niveles de agrupación** (ej. por Genero).
5. Elegir **orden** y **estilos de diseño**.
6. Finalizar y ajustar en **vista Diseño** (tamaños, colores, títulos).

### 5.1.4 Personalización en vista Diseño

| Elemento | Ajuste |
|---|---|
| **Título y logotipo** | Encabezado del informe |
| **Tamaño de campos** | Arrastrar bordes |
| **Formato de números** | Moneda, porcentaje, fechas |
| **Totales** | Controles calculados: `=Sum([Precio])` |
| **Gráficos** | Insertar gráfico sobre datos del informe |
| **Orden de impresión** | Propiedades de la sección |

> **Ejemplo:** un informe "Ventas por Género" que agrupa por género, muestra subtotales de cada uno y un total general al final.

### 5.1.5 Buenas prácticas de informes

| Práctica | Por qué |
|---|---|
| Basar el informe en una consulta | Fácil de actualizar y filtrar |
| Agrupar y totalizar | Lectura rápida de resúmenes |
| Usar fechas y títulos claros | Identificación del documento |
| Formatear números consistentes | Evita errores de interpretación |
| Probar la impresión | Verificar paginación y cortes |

---

## 5.2 Herramientas para visualización de datos

### 5.2.1 ¿Qué es la visualización de datos?

La **visualización de datos** es la representación gráfica de información para hacerla **comprensible de un vistazo**. Un gráfico bien elegido comunica en segundos lo que una tabla demoraría páginas en explicar.

![La visualización convierte filas en lectura rápida](assets/img/03_que_es_visualizacion.png)

*Figura: La visualización convierte filas en lectura rápida*


### 5.2.2 Tipos de gráficos según el objetivo

| Objetivo | Gráfico adecuado |
|---|---|
| Comparar categorías | Barras, columnas |
| Mostrar evolución en el tiempo | Líneas, área |
| Proporciones de un total | Torta, dona, barras 100% |
| Relación entre dos variables | Dispersión |
| Composición de partes | Stacked bars |
| Jerarquías | Treemap, organigrama |

> 💡 **Regla práctica:** elegir primero el **objetivo** (comparar, evolucionar, proporción) y después el gráfico. No al revés.

### 5.2.3 Comparación de herramientas

| Herramienta | Tipo | Ideal para |
|---|---|---|
| **Access** | Informes en la BD | Documentos formales |
| **Excel** | Tablas y gráficos | Análisis rápido |
| **Power BI** | Dashboards empresariales | Indicadores corporativos |
| **Google Looker Studio** | Dashboards en la nube | Compartir con el equipo |

> **En este tema** nos centramos en **Power BI** y **Google Looker Studio** (antes Google Data Studio) para dashboards.

---

## 5.3 Dashboards básicos

### 5.3.1 ¿Qué es un dashboard?

Un **dashboard** (tablero) es una **pantalla que reúne varios indicadores y visualizaciones** en un solo lugar, para monitorear la gestión de un vistazo.

> **Definición funcional:** es el "tablero del auto" de la empresa: velocímetro (ventas), combustible (stock), temperatura (cobranza). Si algo se sale de rango, se ve enseguida.

### 5.3.2 Anatomía de un dashboard

![Anatomía de un dashboard](assets/img/04_anatomia_dashboard.png)

*Figura: Anatomía de un dashboard*


**Componentes de un dashboard:**
1. **KPIs (indicadores clave):** números clave (ventas del mes, % de cumplimiento).
2. **Gráficos:** evolución, comparaciones, proporciones.
3. **Filtros:** por fecha, sucursal, producto.
4. **Resúmenes/tablas:** detalle del detalle.

### 5.3.3 ¿Qué es un KPI?

Un **KPI** (*Key Performance Indicator* — Indicador Clave de Desempeño) es una **métrica que mide el logro de un objetivo**.

| Área | Ejemplo de KPI |
|---|---|
| Ventas | Ventas del mes, ticket promedio |
| Stock | Rotación de inventario, stock agotado |
| Cobranza | Días promedio de cobro, morosidad |
| Clientes | Clientes nuevos, tasa de recompra |
| Producción | Tiempo de ciclo, % de defectos |

> 💡 Un KPI debe ser **medible, relevante y accionable**. Si no sabés qué hacer cuando cambia, no es un buen KPI.

### 5.3.4 Power BI

**Power BI** (Microsoft) es la herramienta de dashboards líder del mercado empresarial.

| Característica | Detalle |
|---|---|
| Conexión de datos | Excel, Access, SQL, servicios web |
| Modelo | Tablas relacionadas (como el Tema 3) |
| Visualizaciones | Amplia galería de gráficos |
| Publicación | Compartir en línea y apps móviles |
| Licencia | Gratuita (Desktop) + planes pagos |

**Flujo de trabajo básico en Power BI:**

![Flujo de trabajo básico en Power BI](assets/img/05_flujo_powerbi.png)

*Figura: Flujo de trabajo básico en Power BI*


### 5.3.5 Google Looker Studio

**Google Looker Studio** (antes Data Studio) es la alternativa gratuita en la nube de Google.

| Característica | Detalle |
|---|---|
| Conexión de datos | Google Sheets, BigQuery, CSV, APIs |
| Compartición | Vínculos en vivo, sin instalar nada |
| Integración | Con ecosistema Google (Sheets, Ads, Analytics) |
| Costo | Gratuito (con límites) |
| Colaboración | Edición simultánea tipo Google Docs |

**Comparativa Power BI vs Looker Studio:**

| Criterio | Power BI | Looker Studio |
|---|---|---|
| Costo | Gratis + planes pagos | Gratuito |
| Dónde corre | Desktop + nube | Solo nube |
| Fuentes de datos | Muy amplias | Google + varias |
| Compartir | Requiere licencia (a veces) | Vínculo simple |
| Curva de aprendizaje | Media-alta | Baja |

---

## 5.4 De los datos a las decisiones

### 5.4.1 El ciclo de la decisión basada en datos

![Ciclo de la decisión basada en datos](assets/img/06_ciclo_decision.png)

*Figura: Ciclo de la decisión basada en datos*


### 5.4.2 Ejemplo aplicado a la librería

1. **Pregunta:** "¿Qué géneros venden más en marzo?"
2. **Datos:** tabla Ventas de la BD.
3. **Análisis:** consulta `SELECT Genero, Sum(Total) FROM Ventas WHERE Mes = 3 GROUP BY Genero`.
4. **Visualización:** dashboard con barras por género.
5. **Decisión:** reforzar stock del género líder y promocionar el que menos vende.
6. **Medición:** comparar ventas del mes siguiente.

### 5.4.3 Errores comunes al visualizar

| Error | Consecuencia |
|---|---|
| Gráfico torta con muchas categorías | Ilegible |
| Escala manipulada | Lectura engañosa |
| Demasiados KPIs | Se pierde el foco |
| Datos desactualizados | Decisiones equivocadas |
| Gráfico sin título | No se entiende el contexto |

> 💡 **Clave:** un buen dashboard responde preguntas, no solo muestra números. Antes de armarlo: *"¿qué decisión voy a tomar con esto?"*

---

## Preguntas de repaso

1. ¿Qué es un informe y en qué se diferencia de una consulta?
2. Describe las partes de un informe en Access.
3. ¿Cuáles son los tipos de informes y cuándo usar cada uno?
4. ¿Qué pasos se siguen para crear un informe en Access?
5. ¿Qué es la visualización de datos y por qué importa?
6. ¿Qué gráfico usarías para comparar categorías? ¿Y para evolución temporal?
7. Compara Access, Excel, Power BI y Looker Studio.
8. ¿Qué es un dashboard y qué componentes tiene?
9. ¿Qué es un KPI? Da 3 ejemplos para una librería.
10. Compara Power BI y Google Looker Studio.
11. Describe el ciclo de decisión basada en datos.
12. Menciona 3 errores comunes al visualizar datos.

---

## Glosario

| Término | Significado |
|---|---|
| **Dashboard** | Tablero de indicadores y visualizaciones para monitorear la gestión |
| **Informe** | Presentación organizada de datos para lectura y análisis |
| **KPI** | Indicador clave que mide el logro de un objetivo |
| **Looker Studio** | Herramienta gratuita de dashboards en la nube de Google |
| **Power BI** | Herramienta de Microsoft para dashboards empresariales |
| **Visualización de datos** | Representación gráfica de la información |
| **Encabezado de informe** | Sección con título, logotipo y datos generales |
| **Grupo** | Agrupación de registros con totales parciales en un informe |
| **Subinforme** | Informe dentro de otro (maestro-detalle) |
| **Total general** | Suma final de los datos del informe |
