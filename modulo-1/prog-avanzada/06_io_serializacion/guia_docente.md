# GUÍA DOCENTE — Unidad 7: Entrada/Salida, Archivos y Serialización

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Leer y escribir** archivos de texto en Java con `try-with-resources`.
2. **Serializar y deserializar** objetos a JSON (Jackson) y binario (`Serializable`).
3. **Comparar** JSON y XML y elegir el formato según el caso.
4. **Explicar** la diferencia entre streams de bytes y caracteres.
5. **Aplicar** buffers para mejorar el rendimiento de E/S.

---

## 2. Plan de clases

### Clase 1 — Archivos (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Dónde quedan los datos cuando apagas la computadora?"* | Debate guiado |
| 20' | Flujo de archivos y persistencia | Slides 3-4 |
| 25' | Escritura y lectura con buffers | Slides 5-6 |
| 20' | Streams: bytes vs caracteres | Slides 11-12 |
| 5' | Cierre | — |

### Clase 2 — Serialización + práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Serialización y deserialización | Slide 7 |
| 20' | JSON con Jackson | Slides 8-9 |
| 10' | JSON vs XML | Slide 10 |
| 10' | Serialización binaria | Slide 13 |
| 25' | **Taller**: persistencia del catálogo en JSON | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. Partir del catálogo de `Producto` de la Unidad 6.
2. Agregar Jackson al `pom.xml`.
3. Implementar `guardarCatalogo(String archivo)` que serialice la lista a JSON.
4. Implementar `cargarCatalogo(String archivo)` que la deserialice.
5. Verificar el ciclo completo: cargar → modificar → guardar → recargar.
6. **Reto extra:** guardar también en CSV manualmente y comparar con JSON (tamaño y legibilidad).

**Criterios de evaluación:**
- Archivos se cierran correctamente (try-with-resources).
- JSON generado es válido (validar en jsonlint).
- El ciclo carga-guarda-carga funciona sin pérdidas.
- Manejo correcto de `IOException`.

---

## 4. Evaluación

- **Taller práctico (50%):** persistencia JSON funcional.
- **Evaluación formativa (20%):** preguntas orales.
- **Prueba escrita (30%):** streams, buffers, serialización.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_flujo_archivos.mmd` — flujo lectura/escritura.
- `assets/mermaid/02_jerarquia_streams.mmd` — jerarquía de streams.
- `assets/mermaid/03_serializacion.mmd` — ciclo de serialización.
- `assets/mermaid/04_json_vs_xml.mmd` — comparativa de formatos.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — *I/O Streams*, *Serialization*.
- FasterXML — *Jackson Project* (github.com/FasterXML).
- Baeldung — *Java File I/O*, *Jackson ObjectMapper*.
