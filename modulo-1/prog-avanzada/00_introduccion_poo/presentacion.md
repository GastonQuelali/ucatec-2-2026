---
marp: true
theme: default
paginate: true
header: "Unidad 1 — Introducción a la Programación Orientada a Objetos"
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

# Programación Orientada a Objetos
## Introducción a la POO Moderna
### Unidad 1
#### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Evolución** — de la programación estructurada a la POO
2. **Los 4 pilares** — abstracción, encapsulamiento, herencia, polimorfismo
3. **Clase vs objeto** — el molde y sus instancias
4. **Ejemplos en Java, Python y C#** — un mismo problema, varios lenguajes

---

## Evolución de los paradigmas

<!-- fuente: assets/mermaid/01_evolucion_paradigmas.mmd -->
![w:910](assets/img/01_evolucion_paradigmas.png)

**POO = agrupar *datos* y *funciones* en objetos** que representan entidades reales.

---

## Los 4 pilares de la POO

<!-- fuente: assets/mermaid/02_pilares_poo.mmd -->
![w:830](assets/img/02_pilares_poo.png)

---

## Pilar 1 y 2: Abstracción y Encapsulamiento

**Abstracción** — modelar lo esencial, ignorar lo irrelevante
- `Libro`: título, autor, ISBN, estado. *(El peso no importa)*

**Encapsulamiento** — ocultar los detalles, exponer interfaz controlada
- `saldo` es privado; solo `depositar()` y `retirar()` lo modifican

> **Regla de oro:** los atributos son **privados**, los métodos **públicos**.

---

## Pilar 3: Herencia

Relación **"es-un"**: la clase hija reutiliza y extiende a la clase padre.

```
Vehiculo  (marca, encender())
 ├── Auto  (puertas, abrirBaul())
 └── Moto  (cascos, cabalgar())
```

> Una Moto **es un** Vehículo: hereda todo y agrega lo propio.

---

## Pilar 4: Polimorfismo

Un mismo nombre, muchos comportamientos:

| Tipo | Dónde | Qué cambia |
|---|---|---|
| **Sobrecarga** | Misma clase | Parámetros |
| **Sobreescritura** | Clase hija | Implementación |

> `hacerSonido()` → Perro: "guau" · Gato: "miau" · Vaca: "muuu"

---

## Clase vs objeto

<!-- fuente: assets/mermaid/03_clase_vs_objeto.mmd -->
![w:830](assets/img/03_clase_vs_objeto.png)

**Clase = plano · Objeto = casa construida con ese plano**

---

## Ejemplo en Java

```java
public class Libro {
    private String titulo;
    private String autor;

    public Libro(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    public void mostrar() {
        System.out.println(titulo + " — " + autor);
    }
}
```

---

## Crear objetos (instancias)

```java
public class Main {
    public static void main(String[] args) {
        Libro l1 = new Libro("Don Quijote", "Cervantes");
        Libro l2 = new Libro("Cien años...", "García Márquez");
        l1.mostrar();
        l2.mostrar();
    }
}
```

> `new Libro(...)` **instancia** la clase: crea un objeto en memoria.

---

## Un problema, varios lenguajes

<!-- fuente: assets/mermaid/04_paradigmas_mixtos.mmd -->
![w:830](assets/img/04_paradigmas_mixtos.png)

---

## Java vs Python vs C#

```java
// Java
public class Usuario {
    private String nombre;
    public Usuario(String n) { this.nombre = n; }
    public String getNombre() { return nombre; }
}
```

```python
# Python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre
```

---

## POO moderna: más que clases

1. **Funcional**: lambdas, streams (código más conciso)
2. **Frameworks**: imponen patrones de diseño
3. **Buenas prácticas**: SOLID, testing, control de versiones

> Veremos todo esto en las próximas unidades.

---

## Resumen

- **POO** agrupa datos + comportamiento en **objetos**
- **4 pilares**: abstracción, encapsulamiento, herencia, polimorfismo
- **Clase** = molde · **Objeto** = instancia
- Los conceptos son **universales** (Java, Python, C#)

---

## Preguntas de repaso

1. ¿Qué problema resolvió la POO frente a la programación estructurada?
2. Nombra los 4 pilares con un ejemplo de cada uno.
3. ¿Clase vs objeto? Da una analogía.
4. ¿Sobrecarga vs sobreescritura?

---

## Gracias

> **Tarea:** crear la clase `Perro` (nombre, raza, método `ladrar()`) y 3 instancias en Java.
