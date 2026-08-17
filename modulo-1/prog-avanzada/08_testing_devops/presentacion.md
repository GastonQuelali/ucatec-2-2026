---
marp: true
theme: default
paginate: true
header: "Unidad 9 — Pruebas, Buenas Prácticas y DevOps Básico"
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

# Pruebas, Buenas Prácticas y DevOps Básico
## Unidad 9
### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Testing automatizado** — JUnit, unitarias vs integración
2. **Documentación y estilo** — JavaDoc, convenciones
3. **Git profesional** — ramas, Pull Requests, colaboración
4. **CI/CD** — pipelines con GitHub Actions

---

## ¿Por qué probar?

> Probar **automáticamente** evita **regresiones**: cambios que rompen lo que ya funcionaba.

| Tipo | Verifica |
|---|---|
| **Unitaria** | Un método aislado |
| **Integración** | Interacción entre componentes |
| **Aceptación** | Todo el sistema |

---

## Flujo de testing

<!-- fuente: assets/mermaid/01_flujo_testing.mmd -->
![w:830](assets/img/01_flujo_testing.png)

---

## JUnit 5

```java
class CalculadoraTest {

    @Test
    void sumarDevuelveLaSuma() {
        Calculadora calc = new Calculadora();
        assertEquals(5, calc.sumar(2, 3));
    }

    @Test
    void dividirPorCeroLanzaExcepcion() {
        Calculadora calc = new Calculadora();
        assertThrows(ArithmeticException.class,
                     () -> calc.dividir(10, 0));
    }
}
```

---

## Estructura AAA

```java
@Test
void retirarDescuentaElSaldo() {
    // Arrange
    Cuenta cuenta = new Cuenta(100.0);

    // Act
    boolean resultado = cuenta.retirar(30.0);

    // Assert
    assertTrue(resultado);
    assertEquals(70.0, cuenta.consultarSaldo());
}
```

---

## JavaDoc

```java
/**
 * Representa una cuenta bancaria.
 *
 * @author Estudiante SIS120
 * @version 1.0
 */
public class CuentaBancaria {

    /** Saldo actual de la cuenta. */
    private double saldo;

    /**
     * Retira dinero si hay saldo suficiente.
     * @param monto cantidad a retirar
     * @return true si la operación se realizó
     */
    public boolean retirar(double monto) { ... }
}
```

---

## Convenciones de estilo

<!-- fuente: assets/mermaid/05_documentacion_estilo.mmd -->
![w:830](assets/img/05_documentacion_estilo.png)

---

## Git workflow

<!-- fuente: assets/mermaid/02_git_workflow.mmd -->
![w:830](assets/img/02_git_workflow.png)

---

## Comandos esenciales

| Comando | Qué hace |
|---|---|
| `git commit -m "msg"` | Punto de control |
| `git checkout -b feature/x` | Nueva rama |
| `git push origin rama` | Sube a GitHub |
| `git pull origin main` | Trae cambios |
| `git log` | Historial |

---

## Trabajo colaborativo en GitHub

1. Cambio en **rama** descriptiva
2. **Pull Request** al terminar
3. **Peer review**: compañeros comentan
4. **Merge** a `main` tras aprobar
5. **GitHub Actions** valida automáticamente

---

## Pipeline CI/CD

<!-- fuente: assets/mermaid/03_pipeline_cicd.mmd -->
![w:830](assets/img/03_pipeline_cicd.png)

---

## GitHub Actions

```yaml
name: Java CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - run: mvn clean test
```

---

## Resumen

- **JUnit**: pruebas unitarias automáticas (AAA)
- **JavaDoc + convenciones**: código profesional
- **Git + GitHub**: ramas, PR, peer review
- **CI/CD**: cada push compila, prueba y (si pasa) despliega

---

## Preguntas de repaso

1. ¿Unitaria vs integración?
2. ¿Qué es AAA?
3. ¿Para qué sirve una Pull Request?
4. ¿Qué hace el pipeline en cada push?

---

## Gracias

> **Tarea:** escribir tests JUnit para `descuento(precio)` y configurar `.github/workflows/ci.yml` en el proyecto.
