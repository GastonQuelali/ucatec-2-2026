---
marp: true
theme: default
paginate: true
header: "Unidad 7 — Entrada/Salida, Archivos y Serialización"
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

# Entrada/Salida, Archivos y Serialización
## Unidad 7
### Ing. Gaston Genaro Quelali Calcina

---

## Agenda

1. **Archivos** — lectura y escritura en Java
2. **Serialización** — JSON, XML, binario
3. **Streams y buffers** — bytes vs caracteres, rendimiento

---

## Flujo de archivos

<!-- fuente: assets/mermaid/01_flujo_archivos.mmd -->
![w:830](assets/img/01_flujo_archivos.png)

> **Persistencia:** los datos sobreviven a la ejecución.

---

## Escritura

```java
try (BufferedWriter bw =
        new BufferedWriter(new FileWriter("productos.txt"))) {
    bw.write("Libro;25.5");
    bw.newLine();
    bw.write("Cuaderno;8.0");
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

---

## Lectura

```java
try (BufferedReader br =
        new BufferedReader(new FileReader("productos.txt"))) {
    String linea;
    while ((linea = br.readLine()) != null) {
        String[] partes = linea.split(";");
        System.out.println(partes[0] + " | " + partes[1]);
    }
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

> Siempre `try-with-resources` → cierre automático.

---

## Serialización

<!-- fuente: assets/mermaid/03_serializacion.mmd -->
![w:830](assets/img/03_serializacion.png)

**Serializar** = objeto → formato · **Deserializar** = formato → objeto

---

## JSON con Jackson

```java
ObjectMapper mapper = new ObjectMapper();

// Objeto → JSON
Producto p = new Producto(1, "Libro", 25.5);
String json = mapper.writeValueAsString(p);
// {"id":1,"nombre":"Libro","precio":25.5}

// JSON → Objeto
Producto restaurado = mapper.readValue(json, Producto.class);
```

---

## JSON vs XML

<!-- fuente: assets/mermaid/04_json_vs_xml.mmd -->
![w:830](assets/img/04_json_vs_xml.png)

---

## JSON vs XML (tabla)

| Característica | JSON | XML |
|---|---|---|
| Legibilidad | Alta | Media |
| Tamaño | Compacto | Verboso |
| Uso típico | APIs REST | Documentos |

---

## Serialización binaria (Java)

```java
public class Producto implements Serializable {
    private static final long serialVersionUID = 1L;
    // atributos, getters, setters...
}

try (ObjectOutputStream oos =
        new ObjectOutputStream(new FileOutputStream("p.bin"))) {
    oos.writeObject(new Producto(1, "Libro", 25.5));
}
```

---

## Streams: bytes vs caracteres

<!-- fuente: assets/mermaid/02_jerarquia_streams.mmd -->
![w:830](assets/img/02_jerarquia_streams.png)

| Familia | Para | Ejemplos |
|---|---|---|
| `Stream` | Bytes (binarios) | FileInput/OutputStream |
| `Reader/Writer` | Caracteres (texto) | FileReader, BufferedReader |

---

## ¿Por qué buffers?

**Buffer = memoria intermedia** que transfiere en bloques:

```java
// LENTO: byte a byte
while ((c = fr.read()) != -1) { ... }

// RÁPIDO: por líneas/bloques
while ((linea = br.readLine()) != null) { ... }
```

> Envolver con `Buffered*` mejora el rendimiento de E/S.

---

## Resumen

- Archivos: `FileWriter`/`FileReader` + `Buffered*`
- Serialización: JSON (Jackson) para APIs, binaria para interna
- Streams: bytes vs caracteres
- Buffers: menos operaciones de E/S → más rápido

---

## Preguntas de repaso

1. ¿`FileReader` vs `FileInputStream`?
2. ¿Qué es serializar/deserializar?
3. ¿JSON o XML? ¿Cuándo?
4. ¿Qué aporta un buffer?

---

## Gracias

> **Tarea:** guardar la lista de productos de la unidad anterior en JSON con Jackson y recuperarla al iniciar el programa.
