# GUÍA DOCENTE — Unidad 10: Tendencias y Temas Emergentes

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Diferenciar** concurrencia y paralelismo y usar hilos/ExecutorService en Java.
2. **Explicar** la arquitectura de microservicios y consumir APIs REST con `HttpClient`.
3. **Aplicar** principios de seguridad y ética en el desarrollo.
4. **Practicar** TDD y mockeo con JUnit y Mockito.

---

## 2. Plan de clases

### Clase 1 — Concurrencia y microservicios (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Por qué una app de pedidos atiende a miles a la vez?"* | Debate guiado |
| 20' | Concurrencia vs paralelismo | Slides 3-5 |
| 20' | Hilos y ExecutorService | Slides 6-7 |
| 25' | Microservicios y APIs REST | Slides 8-11 |
| 5' | Cierre | — |

### Clase 2 — Seguridad, TDD y práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Seguridad y ética + OWASP | Slides 12-13 |
| 15' | TDD: RED-GREEN-REFACTOR | Slide 14 |
| 15' | Mockeo con Mockito | Slide 15 |
| 35' | **Taller**: consumir API + test | Guía práctica (abajo) |
| 5' | Cierre de asignatura | — |

---

## 3. Taller práctico (guía para el alumno)

1. Consumir una API pública (ej. **JSONPlaceholder**: `https://jsonplaceholder.typicode.com/todos`).
2. Con `HttpClient`, obtener los datos y mostrar los 3 primeros títulos.
3. Deserializar la respuesta a una lista de objetos con **Jackson** (retoma la Unidad 6).
4. Escribir un **test JUnit** para el método que convierte JSON → objeto.
5. **Reto extra (TDD):** escribir primero el test de un `descuento()` y luego la implementación (RED-GREEN).
6. **Reto extra 2:** usar **Mockito** para probar un `ServicioProducto` que depende de un repositorio.

**Criterios de evaluación:**
- La API se consume y la respuesta se deserializa correctamente.
- Tests JUnit que pasan (verificación con `mvn test`).
- TDD demostrado en al menos un método.
- Uso de mock para aislar una dependencia.

---

## 4. Evaluación

- **Taller práctico (40%):** consumo de API + tests.
- **Proyecto integrador (40%):** se evalúa en la semana final (POO + excepciones + testing).
- **Evaluación formativa (20%):** preguntas orales y participación.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_concurrencia_paralela.mmd` — concurrencia vs paralelismo.
- `assets/mermaid/02_microservicios.mmd` — arquitectura de microservicios.
- `assets/mermaid/03_api_rest.mmd` — flujo de una API REST.
- `assets/mermaid/04_ciclo_tdd.mmd` — ciclo TDD.
- `assets/mermaid/05_seguridad_etica.mmd` — seguridad y ética.

---

## 6. Recursos complementarios

- Oracle — *Java Concurrency Tutorials*.
- GitHub — *JSONPlaceholder* (demo API).
- OWASP — *Top 10* (owasp.org).
- Kent Beck. *Test Driven Development: By Example*.
- Mockito — *Docs* (site.mockito.org).
