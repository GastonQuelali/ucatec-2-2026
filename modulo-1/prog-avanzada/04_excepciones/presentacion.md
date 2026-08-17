---
marp: true
theme: default
paginate: true
header: "Unidad 5 — Manejo de Errores y Excepciones"
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

# Manejo de Errores y Excepciones
## Unidad 5
### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Jerarquía de excepciones** — Error, Exception, RuntimeException
2. **try / catch / finally** — el flujo de manejo
3. **Excepciones personalizadas** — contexto de negocio
4. **Logging y debugging** — registrar y diagnosticar

---

## Jerarquía de excepciones

<!-- fuente: assets/mermaid/01_jerarquia_excepciones.mmd -->
![w:700](assets/img/01_jerarquia_excepciones.png)

---

## Las tres ramas

| Rama | Ejemplos | ¿Obligatorio? |
|---|---|---|
| `Error` | OutOfMemory, StackOverflow | No |
| `Exception` (checked) | IOException, SQLException | **Sí** |
| `RuntimeException` | NPE, Arithmetic | No |

> **Checked** obliga a capturar; **unchecked** indica error de lógica.

---

## try / catch / finally

<!-- fuente: assets/mermaid/02_flujo_try_catch.mmd -->
![w:830](assets/img/02_flujo_try_catch.png)

```java
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("División por cero");
} finally {
    System.out.println("Siempre se ejecuta");
}
```

---

## Manejo avanzado

**Varios catch (específico → general):**

```java
try {
    Integer.parseInt(texto);
} catch (NumberFormatException e) {
    // específica
} catch (RuntimeException e) {
    // general
}
```

**Multi-catch:**

```java
} catch (IOException | SQLException e) {
    System.out.println(e.getMessage());
}
```

---

## try-with-resources

```java
try (BufferedReader br =
        new BufferedReader(new FileReader("datos.txt"))) {
    String linea = br.readLine();
} catch (IOException e) {
    System.out.println("Error al leer: " + e.getMessage());
}
// El recurso se cierra SOLO
```

---

## throw vs throws

| Palabra | Significado |
|---|---|
| `throw` | Lanza una excepción en ese punto |
| `throws` | Declara que el método puede lanzarla |

```java
public void retirar(double monto) throws SaldoInsuficienteException {
    if (monto > this.saldo) {
        throw new SaldoInsuficienteException("Saldo insuficiente");
    }
    this.saldo -= monto;
}
```

---

## Excepciones personalizadas

Comunican **contexto del negocio**:

```java
public class SaldoInsuficienteException extends RuntimeException {
    public SaldoInsuficienteException(String mensaje) {
        super(mensaje);
    }
}
```

> `SaldoInsuficienteException` dice mucho más que `IllegalStateException`.

---

## Logging con Log4j

```java
private static final Logger log =
        LogManager.getLogger(Procesador.class);

log.info("Procesando: {}", nombre);
log.error("Error al procesar {}", nombre, e);
```

| Nivel | Uso |
|---|---|
| DEBUG | Detalles de desarrollo |
| INFO | Eventos normales |
| WARN | Sospechoso |
| ERROR | Fallo |

---

## Debugging con el IDE

<!-- fuente: assets/mermaid/03_ciclo_depuracion.mmd -->
![w:830](assets/img/03_ciclo_depuracion.png)

**Breakpoint · Step Over · Step Into · Step Out · Watches**

---

## Logging vs Debugging

> **Logging** responde *"¿qué pasó?"* — registro permanente
> **Debugging** responde *"¿por qué pasó?"* — análisis interactivo

Ambos son **indispensables** en proyectos reales.

---

## Resumen

- `Error` = grave · `Exception` = checked · `RuntimeException` = lógica
- `try/catch/finally` + `throw`/`throws`
- Excepciones personalizadas = contexto de negocio
- Logs para registrar, debugger para diagnosticar

---

## Preguntas de repaso

1. ¿Checked vs unchecked?
2. ¿Para qué sirve `finally`?
3. ¿`throw` vs `throws`?
4. ¿Qué hace un breakpoint?

---

## Gracias

> **Tarea:** crear `LibroNoDisponibleException` y usarla en un método `prestar()`. Agregar logging INFO/ERROR.
