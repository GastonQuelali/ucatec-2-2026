# GUÍA DOCENTE — Unidad 5: Manejo de Errores y Excepciones

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Explicar** la jerarquía `Throwable` → `Exception`/`RuntimeException`/`Error`.
2. **Aplicar** `try`/`catch`/`finally`, multi-catch y try-with-resources.
3. **Diferenciar** `throw` de `throws` y propagar excepciones.
4. **Crear** excepciones personalizadas con contexto de negocio.
5. **Usar** logging (SLF4J/Log4j) y técnicas básicas de debugging.

---

## 2. Plan de clases

### Clase 1 — Jerarquía y try/catch (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Qué pasa si un archivo no existe y nadie maneja el error?"* | Debate guiado |
| 20' | Jerarquía de excepciones | Slides 3-5 |
| 25' | try/catch/finally y manejo avanzado | Slides 6-9 |
| 20' | throw/throws con ejemplos | Slide 10 |
| 5' | Cierre | — |

### Clase 2 — Excepciones propias, logging y práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Excepciones personalizadas | Slides 11-12 |
| 15' | Logging con Log4j | Slides 13-14 |
| 15' | Debugging con el IDE | Slide 15 |
| 35' | **Taller**: banco con excepciones + logging | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. Crear `CuentaBancaria` con `retirar()` que lance `SaldoInsuficienteException` si no hay saldo.
2. Crear `CuentaNoEncontradaException` para el método `transferir()`.
3. Agregar logging `INFO` (depósitos/retiros) y `ERROR` (fallos) con Log4j.
4. Probar el flujo y usar el **debugger** (breakpoint) para ver cómo cambia `saldo`.
5. **Reto extra:** convertir `SaldoInsuficienteException` a *checked* y ver qué obliga a cambiar el compilador.

**Criterios de evaluación:**
- Jerarquía de excepciones correcta y justificada.
- Uso correcto de `throw`, `throws`, `try-with-resources`.
- Logs con niveles adecuados.
- Capacidad de depurar con breakpoints.

---

## 4. Evaluación

- **Taller práctico (50%):** banco con excepciones + logging funcional.
- **Evaluación formativa (20%):** preguntas orales.
- **Prueba escrita (30%):** jerarquía, throw/throws, try-with-resources.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_jerarquia_excepciones.mmd` — jerarquía Throwable.
- `assets/mermaid/02_flujo_try_catch.mmd` — flujo try/catch/finally.
- `assets/mermaid/03_ciclo_depuracion.mmd` — ciclo de depuración.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — *Exceptions*.
- Apache Log4j 2 — *Manual de configuración*.
- Baeldung — *Exception Handling in Java*.
