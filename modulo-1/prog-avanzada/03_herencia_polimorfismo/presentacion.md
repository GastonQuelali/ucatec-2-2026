---
marp: true
theme: default
paginate: true
header: "Unidad 4 — Composición, Herencia y Polimorfismo"
footer: "UCatec · Programación Avanzada"
size: 16:9
style: |
  section { font-size: 26px; }
  section.title h1 { font-size: 58px; color: #0b4f8a; }
  section.title h2 { font-size: 30px; color: #555; }
  h2 { color: #0b4f8a; }
  table { font-size: 18px; }
  blockquote { background: #eef4fb; border-left: 5px solid #0b4f8a; padding: 8px 14px; }
  .columns { display: flex; gap: 30px; }
  .columns > div { flex: 1; }
  img { display: block; margin: 0 auto; }
  pre { font-size: 18px; }
---

<!-- _class: title -->

# Composición, Herencia y Polimorfismo
## Unidad 4
### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Relaciones entre clases** — asociación, composición, agregación
2. **Herencia** — "es-un", reutilización, extensibilidad
3. **Polimorfismo** — sobrecarga y sobreescritura
4. **Interfaces y clases abstractas**
5. **Principios SOLID**

---

## Relaciones entre clases

<!-- fuente: assets/mermaid/01_relaciones_clases.mmd -->
![w:830](assets/img/01_relaciones_clases.png)

---

## Asociación vs Agregación vs Composición

| Relación | Significado | ¿Existe sin el otro? |
|---|---|---|
| **Asociación** | Se usan mutuamente | Sí |
| **Agregación** | "Tiene-un" (parte) | Sí |
| **Composición** | "Tiene-un" (ciclo ligado) | No |

> `Pedido` (composición) → `LineaPedido` · `Equipo` (agregación) → `Jugador`

---

## Herencia: "es-un"

<!-- fuente: assets/mermaid/02_jerarquia_herencia.mmd -->
![w:700](assets/img/02_jerarquia_herencia.png)

```java
public class Perro extends Animal {
    public Perro(String nombre) { super(nombre); }
    public void moverCola() { ... }
}
```

---

## ¿Herencia o composición?

| Criterio | Herencia | Composición |
|---|---|---|
| Relación | Es-un | Tiene-un |
| Acoplamiento | Alto | Bajo |
| Cambios | Afectan a las hijas | Aislados |

> **Preferir composición** sobre herencia cuando sea posible.

---

## Polimorfismo: sobrecarga vs sobreescritura

<!-- fuente: assets/mermaid/03_sobrecarga_sobreescritura.mmd -->
![w:830](assets/img/03_sobrecarga_sobreescritura.png)

---

## Polimorfismo en acción

<!-- fuente: assets/mermaid/05_polimorfismo.mmd -->
![w:830](assets/img/05_polimorfismo.png)

```java
Figura f = new Circulo();
f.dibujar();  // "Dibujando un círculo"
```

> **Sin `if/else` por tipo:** cada figura hace lo suyo.

---

## Interface vs Clase abstracta

<!-- fuente: assets/mermaid/04_interface_vs_abstracta.mmd -->
![w:830](assets/img/04_interface_vs_abstracta.png)

---

## En código

```java
public interface Volador { void volar(); }

public abstract class Vehiculo {
    protected String marca;
    public Vehiculo(String marca) { this.marca = marca; }
    public abstract void mover();
}

public class Avion extends Vehiculo implements Volador {
    public void mover() { ... }
    public void volar() { ... }
}
```

> Una clase **hereda de UNA abstracta** e **implementa VARIAS interfaces**.

---

## Principios SOLID

<!-- fuente: assets/mermaid/06_solid.mmd -->
![w:830](assets/img/06_solid.png)

---

## Antes y después (SRP + DIP)

**Violación — `Factura` hace de todo:**

```java
public class Factura {
    public double calcularTotal() { ... }
    public void guardarEnBD() { ... }
    public void enviarEmail() { ... }
}
```

---

## Después (SRP + DIP)

```java
public interface RepositorioFactura { void guardar(Factura f); }

public class FacturaRepositorioBD implements RepositorioFactura { ... }

public class Factura {
    private RepositorioFactura repositorio;  // DIP
    public Factura(RepositorioFactura repositorio) {
        this.repositorio = repositorio;
    }
    public double calcularTotal() { ... }
}
```

---

## Resumen

- **Asociación / Agregación / Composición** — grado de acoplamiento
- **Herencia** — "es-un"; **composición** — "tiene-un"
- **Polimorfismo** — sobrecarga + sobreescritura
- **Interfaces** — contrato; **abstractas** — base con estado
- **SOLID** — 5 principios de diseño robusto

---

## Preguntas de repaso

1. ¿Agregación vs composición?
2. ¿Cuándo usar herencia y cuándo composición?
3. ¿Interface vs clase abstracta?
4. Nombra los 5 principios SOLID.

---

## Gracias

> **Tarea:** refactorizar la clase "todo-en-uno" aplicando SRP, usando interfaces y una clase que dependa de la abstracción.
