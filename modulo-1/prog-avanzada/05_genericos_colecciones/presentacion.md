---
marp: true
theme: default
paginate: true
header: "Unidad 6 — Genéricos, Colecciones y Estructuras Avanzadas"
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

# Genéricos, Colecciones y Estructuras Avanzadas
## Unidad 6
### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Programación genérica** — `T` como parámetro de tipo
2. **Colecciones** — List, Set, Map, Queue
3. **¿Cuál elegir?** — según orden, duplicados y velocidad
4. **Iteradores y Streams** — recorrido eficiente

---

## Genéricos: el problema

**Antes (sin genéricos):**

```java
List lista = new ArrayList();
lista.add("Hola");
String s = (String) lista.get(0);  // cast manual
```

**Con genéricos:**

```java
List<String> lista = new ArrayList<>();
String s = lista.get(0);  // automático y seguro
```

> El error se detecta **en compilación**, no en ejecución.

---

## Clase genérica

<!-- fuente: assets/mermaid/03_generics.mmd -->
![w:560](assets/img/03_generics.png)

```java
public class Caja<T> {
    private T contenido;
    public void guardar(T valor) { this.contenido = valor; }
    public T obtener() { return contenido; }
}
```

---

## Jerarquía de colecciones

<!-- fuente: assets/mermaid/01_jerarquia_colecciones.mmd -->
![w:830](assets/img/01_jerarquia_colecciones.png)

---

## ¿Cuál elegir?

<!-- fuente: assets/mermaid/02_list_set_map.mmd -->
![w:830](assets/img/02_list_set_map.mmd)

---

## List vs Set vs Map

```java
List<String> nombres = new ArrayList<>();
nombres.add("Ana"); nombres.add("Ana");  // duplicado OK
String primero = nombres.get(0);

Set<String> alumnos = new HashSet<>();
alumnos.add("Ana"); alumnos.add("Ana");  // se ignora
System.out.println(alumnos.size());       // 1

Map<String, Double> precios = new HashMap<>();
precios.put("Libro", 25.5);
Double p = precios.get("Libro");          // 25.5
```

---

## Tabla comparativa

| Estructura | Duplicados | Ordenado | Acceso |
|---|---|---|---|
| `List` | Sí | Por inserción | Índice |
| `Set` | No | Según tipo | Valor |
| `Map` | Claves únicas | Según tipo | Clave |
| `Queue` | Sí | FIFO/prioridad | Primero |

---

## Iteradores

<!-- fuente: assets/mermaid/04_iteradores.mmd -->
![w:830](assets/img/04_iteradores.png)

```java
Iterator<Producto> it = productos.iterator();
while (it.hasNext()) {
    Producto p = it.next();
    if (p.getStock() == 0) it.remove();  // seguro
}
```

---

## For-each

```java
for (Producto p : productos) {
    System.out.println(p.getNombre());
}
```

> ⚠️ `for-each` NO permite eliminar. Para eso, usar `Iterator`.

---

## Streams (Java 8+)

```java
List<String> baratos = productos.stream()
        .filter(p -> p.getPrecio() < 10)
        .map(Producto::getNombre)
        .toList();

productos.stream()
        .sorted(Comparator.comparing(Producto::getPrecio))
        .limit(3)
        .forEach(p -> System.out.println(p.getNombre()));
```

---

## Operaciones de Streams

| Operación | Qué hace |
|---|---|
| `filter` | Filtra por condición |
| `map` | Transforma elementos |
| `sorted` | Ordena |
| `limit` | Toma N elementos |
| `collect` | Recolecta en lista/set |

---

## Eficiencia

> Elegir bien la estructura importa:
> `Map` busca por clave en **O(1)**, una lista en **O(n)**.

**Regla:** primero decide qué estructura, después el algoritmo.

---

## Resumen

- **Genéricos** = tipos como parámetro (seguridad en compilación)
- **List** ordenada/duplicados · **Set** únicos · **Map** clave→valor
- **Iterator** permite recorrer y eliminar de forma segura
- **Streams** para manipulación funcional y concisa

---

## Preguntas de repaso

1. ¿Qué evitan los genéricos?
2. ¿List vs Set vs Map?
3. ¿Por qué `for-each` no puede eliminar?
4. ¿Qué hace `filter`? ¿Y `map`?

---

## Gracias

> **Tarea:** catálogo con `Map<String, Double>`, calcular el producto más caro usando Streams.
