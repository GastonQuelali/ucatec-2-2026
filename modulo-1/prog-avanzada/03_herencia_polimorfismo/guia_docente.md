# GUÍA DOCENTE — Unidad 4: Composición, Herencia y Polimorfismo

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Distinguir** asociación, agregación y composición y aplicarlas en código.
2. **Usar** herencia para reutilizar y extender clases, decidiendo cuándo preferir composición.
3. **Explicar y aplicar** polimorfismo mediante sobrecarga y sobreescritura.
4. **Decidir** entre interfaces y clases abstractas según el diseño.
5. **Aplicar** los principios SOLID, especialmente SRP y DIP.

---

## 2. Plan de clases

### Clase 1 — Relaciones y herencia (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Un auto 'es un' vehículo o 'tiene un' motor?"* | Debate guiado |
| 20' | Asociación, agregación y composición | Slides 3-5 |
| 20' | Herencia y jerarquía de clases | Slides 6-7 |
| 20' | Herencia vs composición + código | Slides 8 + ejemplos |
| 10' | Mini-ejercicio: clasificar relaciones | — |

### Clase 2 — Polimorfismo, interfaces y SOLID (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Repaso y polimorfismo | Slides 9-10 |
| 20' | Interfaces vs clases abstractas | Slides 11-13 |
| 20' | SOLID con ejemplos | Slides 14-16 |
| 25' | **Taller**: refactor con SRP + DIP | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. Partir de una clase `Factura` que calcula total, guarda en BD y envía email (todo en uno).
2. **Aplicar SRP:** separar en `Factura` (cálculo), `FacturaRepositorioBD` (persistencia) y `NotificadorEmail` (envío).
3. **Aplicar DIP:** hacer que `Factura` dependa de `RepositorioFactura` (interface) recibida por constructor.
4. **Aplicar polimorfismo:** crear `NotificadorEmail` y `NotificadorSMS` que implementen la interface `Notificador`.
5. **Reto extra:** cambiar el repositorio por `FacturaRepositorioMemoria` sin tocar la clase `Factura` (demuestra Open/Closed).

**Criterios de evaluación:**
- Relaciones bien modeladas (composición en `Pedido`→`LineaPedido`).
- Uso correcto de `extends`, `implements`, `@Override` y `super`.
- El refactor demuestra SRP y DIP con código que compila.

---

## 4. Evaluación

- **Taller práctico (50%):** refactor SOLID funcional.
- **Evaluación formativa (20%):** mini-ejercicio de relaciones.
- **Prueba escrita (30%):** herencia, polimorfismo, interfaces y SOLID.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_relaciones_clases.mmd` — asociación/agregación/composición + herencia.
- `assets/mermaid/02_jerarquia_herencia.mmd` — jerarquía Animal.
- `assets/mermaid/03_sobrecarga_sobreescritura.mmd` — polimorfismo.
- `assets/mermaid/04_interface_vs_abstracta.mmd` — interface vs abstracta.
- `assets/mermaid/05_polimorfismo.mmd` — polimorfismo en acción.
- `assets/mermaid/06_solid.mmd` — principios SOLID.

---

## 6. Recursos complementarios

- Oracle Java Tutorials — *Interfaces*, *Inheritance*, *Polymorphism*.
- Martin, R. *Agile Software Development* (cap. SOLID).
- Deitel & Deitel. *Java: How to Program* (cap. 9-10).
