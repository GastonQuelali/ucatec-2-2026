# FOROS — PROGRAMACIÓN AVANZADA (SIS120)

**Autor:** Ing. Gaston Genaro Quelali Calcina

---

**Contenido:**
- [¿Cómo usar este documento?](#cómo-usar-este-documento)
- [Unidad 0 — Foros: Introducción a la POO](#unidad-0--foros-introducción-a-la-poo)
- [Unidad 1 — Foros: Clases y Objetos](#unidad-1--foros-clases-y-objetos)
- [Unidad 2 — Foros: UML y Diseño](#unidad-2--foros-uml-y-diseño)
- [Unidad 3 — Foros: Herencia y Polimorfismo](#unidad-3--foros-herencia-y-polimorfismo)
- [Unidad 4 — Foros: Manejo de Excepciones](#unidad-4--foros-manejo-de-excepciones)
- [Unidad 5 — Foros: Genéricos y Colecciones](#unidad-5--foros-genéricos-y-colecciones)
- [Unidad 6 — Foros: E/S y Serialización](#unidad-6--foros-es-y-serialización)
- [Unidad 7 — Foros: GUI y Manejo de Eventos](#unidad-7--foros-gui-y-manejo-de-eventos)
- [Unidad 8 — Foros: Testing y DevOps](#unidad-8--foros-testing-y-devops)
- [Unidad 9 — Foros: Tendencias y Temas Emergentes](#unidad-9--foros-tendencias-y-temas-emergentes)

---

## ¿Cómo usar este documento?

Cada unidad del programa tiene **un foro recomendado** (con consigna completa y rúbrica) y **tres opciones alternativas** (con consigna breve) para que el docente elija según el perfil del grupo o la carrera.

**Reglas generales de participación (aplican a todos los foros):**

| Regla | Recomendación |
|---|---|
| Extensión | 150-250 palabras por participación |
| Interacción | Responder al menos a 1 compañero |
| Fuentes | Citar teoría de la materia u otras fuentes |
| Plazo | Ventana de 1 semana desde la apertura |
| Peso | Según el plan de evaluación continua |

---

## Unidad 0 — Foros: Introducción a la POO

### Foro recomendado: ¿Por qué programar orientado a objetos?

**Objetivo de aprendizaje:** justificar el paso de la programación estructurada a la POO usando los pilares (encapsulamiento, abstracción, herencia, polimorfismo) y ejemplos del mundo real.

**Situación/contexto:** una empresa con un sistema antiguo en COBOL y hojas de cálculo quiere modernizarse. Un consultor propone reescribirlo en Java con POO. El dueño pregunta: *"¿qué ganamos realmente?"*.

**Preguntas guía:**
1. ¿Qué problemas concretos de los sistemas estructurados resuelve la POO?
2. Elige un caso del curso (una cuenta bancaria, una biblioteca): ¿cómo modelas un objeto real y qué ventaja tiene sobre una tabla de datos suelta?
3. ¿Cuál de los 4 pilares te parece más importante y por qué?
4. ¿Qué riesgos o costos tiene adoptar la POO en un proyecto viejo?

**Consigna de participación:** defender tu respuesta con al menos 2 argumentos y un ejemplo modelado como clase, y comentar el modelo de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Argumentos | 2+ sólidos y con base teórica | Válidos pero generales | Débiles |
| Ejemplo como clase | Bien modelado y pertinente | Aceptable | Ausente o confuso |
| Pilares | Los relaciona correctamente | Los menciona | No los usa |
| Interacción | Comenta con aporte | Comenta brevemente | No comenta |

### Opciones adicionales

- **Opción 1 — Paradigmas en la vida real:** busca un ejemplo de cada paradigma (imperativo, funcional, orientado a objetos, mixto) en programas o apps que uses a diario y explica cuál predomina y por qué.
- **Opción 2 — El mundo modelado como clases:** identifica 5 objetos reales de tu entorno (una persona, un curso, un producto) y describe clase, atributos y métodos de cada uno.
- **Opción 3 — Java vs otros lenguajes POO:** compara Java con C# o Python en la forma de manejar encapsulamiento y memoria, y argumenta cuál elegirías para un proyecto dado.

---

## Unidad 1 — Foros: Clases y Objetos

### Foro recomendado: Diseña la clase de tu objeto favorito

**Objetivo de aprendizaje:** aplicar la sintaxis completa de una clase (atributos, constructores, encapsulamiento, modificadores de acceso) a un caso elegido por el estudiante.

**Situación/contexto:** el equipo necesita clases bien diseñadas para un sistema nuevo. Tu tarea es modelar un objeto de tu entorno y justificar cada decisión de diseño.

**Preguntas guía:**
1. ¿Qué objeto real elegiste y qué atributos y métodos lo definen?
2. ¿Qué atributos son privados y cuáles públicos? ¿Por qué?
3. ¿Qué constructores definiste y cómo evitamos estados inválidos?
4. ¿Cómo representa tu clase en UML el diagrama correspondiente?

**Consigna de participación:** publicar la clase (código) + su diagrama de clases, y proponer una mejora al diseño de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Modelado | Atributos y métodos coherentes | Aceptable | Incompleto |
| Encapsulamiento | Uso correcto de `private` + getters/setters | Parcial | Público todo |
| Constructores | 1+ y evita estados inválidos | Existen | Ausentes |
| UML | Diagrama correcto | Aceptable | Ausente |
| Interacción | Sugiere mejora real | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Modificadores de acceso:** explica con un ejemplo cuándo usar `public`, `protected`, `package-private` y `private`, y qué pasaría si todo fuera público.
- **Opción 2 — Ciclo de vida y Garbage Collector:** narra el ciclo de vida completo de un objeto en un programa (declaración → `new` → uso → liberación) y qué papel cumple el GC.
- **Opción 3 — Maven vs Gradle:** para un proyecto real de la materia, justifica cuál herramienta de gestión de dependencias usarías y qué bibliotecas (JUnit, Jackson) incorporarías.

---

## Unidad 2 — Foros: UML y Diseño

### Foro recomendado: Del problema al diseño: un sistema de biblioteca

**Objetivo de aprendizaje:** aplicar los diagramas de casos de uso, clases y secuencia para diseñar un sistema pequeño y traducirlo a código.

**Situación/contexto:** se te pide diseñar el sistema de préstamos de una biblioteca antes de programar.

**Preguntas guía:**
1. ¿Quiénes son los actores y qué casos de uso tiene el sistema?
2. ¿Qué clases, atributos y relaciones (asociación, agregación) identificas?
3. Dibuja el diagrama de secuencia de un préstamo exitoso y uno que falle (libro ya prestado).
4. ¿Qué decisiones de diseño tomaste primero y por qué?

**Consigna de participación:** publicar los 3 diagramas (casos de uso, clases, secuencia), justificar las decisiones y validar los diagramas de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Casos de uso | Completos y con actores correctos | Parciales | Ausentes |
| Diagrama de clases | Relaciones correctas | Algunas correctas | Incorrectas |
| Secuencia | Incluye caso feliz y fallo | Solo caso feliz | Ausente |
| Justificación | Decisiones argumentadas | Mencionadas | Sin explicar |
| Interacción | Valida y mejora | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Singleton vs múltiples instancias:** ¿cuándo es correcto un Singleton (ej. conexión a BD) y cuándo es un anti-patrón? Argumenta con pros y contras.
- **Opción 2 — Factory o Strategy:** elige un problema (ej. notificaciones por email/SMS/WhatsApp) y decide qué patrón usarías, justificando por qué el otro no conviene.
- **Opción 3 — Un diagrama mal hecho:** busca o crea un diagrama de clases con errores típicos (relaciones invertidas, multiplicidades mal puestas) y corrígelo explicando cada corrección.

---

## Unidad 3 — Foros: Herencia y Polimorfismo

### Foro recomendado: Diseña una jerarquía con interface o clase abstracta

**Objetivo de aprendizaje:** decidir entre herencia de clase e implementación de interfaces, y aplicar polimorfismo para escribir código extensible.

**Situación/contexto:** necesitas modelar `Figura` (círculo, rectángulo, triángulo) con un método `dibujar()` y `calcularArea()` que se comporte distinto en cada tipo.

**Preguntas guía:**
1. ¿Usarías una clase abstracta o una interface? ¿Por qué?
2. ¿Qué métodos son comunes (heredados) y cuáles abstractos?
3. ¿Cómo aprovechas el polimorfismo en un método que recibe una lista de figuras?
4. ¿Qué ventaja de SOLID se respeta con este diseño?

**Consigna de participación:** publicar la jerarquía (código + diagrama), explicar la decisión abstracta/interface y refactorizar la propuesta de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Decisión abstracta/interface | Justificada | Mencionada | Ausente |
| Herencia | Bien aplicada | Parcial | Mal usada |
| Polimorfismo | Demostrado en código | Presente | Ausente |
| SOLID | Relaciona al menos 1 principio | Lo menciona | No lo usa |
| Interacción | Refactoriza con aporte | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Sobrecarga vs sobreescritura:** con ejemplos de código, explica las diferencias entre sobrecargar y sobreescribir un método y cuándo usarías cada una.
- **Opción 2 — Composición sobre herencia:** investiga el principio *"favor composition over inheritance"* y da un ejemplo real donde una composición sea mejor que heredar.
- **Opción 3 — Los 5 principios SOLID:** elige 2 principios, explícalos con un ejemplo de código antes/después y qué problema evitan.

---

## Unidad 4 — Foros: Manejo de Excepciones

### Foro recomendado: Un crash inesperado en producción

**Objetivo de aprendizaje:** diseñar una estrategia de manejo de errores para un caso real y distinguir excepciones checked vs unchecked.

**Situación/contexto:** una app bancaria muestra la pantalla de error fatal cuando no hay conexión a la base de datos, y un dato mal escrito del usuario tumba todo el flujo.

**Preguntas guía:**
1. ¿Qué excepciones son previsibles (checked) y cuáles imprevistas (unchecked)? Clasifica los casos del escenario.
2. ¿Qué método usarías: `try/catch/finally` o `try-with-resources`? Justifica con el caso.
3. ¿Cuándo crearías una excepción propia (ej. `FondosInsuficientesException`)?
4. ¿Cómo registras (logs) el error para depurarlo después?

**Consigna de participación:** publicar el código que maneja el error (con excepción propia si aplica), explicar la estrategia y criticar la de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Clasificación | Correcta y argumentada | Parcial | Confusa |
| Técnica usada | Adecuada y bien usada | Aceptable | Inadecuada |
| Excepción propia | Bien diseñada | Existe | Ausente |
| Logs | Con buen nivel de detalle | Básico | Sin logs |
| Interacción | Crítica constructiva | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — No tragar la excepción:** investiga el anti-patrón de *catch vacío* o *catch + printStackTrace* y explica qué problemas genera y cómo corregirlo.
- **Opción 2 — Jerarquía de excepciones:** dibuja (con texto) la jerarquía `Throwable → Exception/Error → ...` y explica en qué rama vive `IOException`, `RuntimeException` y `StackOverflowError`.
- **Opción 3 — Depuración en acción:** cuenta una vez que depuraste un error (con logs, IDE debugger o pila de llamadas) y qué pasos seguiste para encontrarlo.

---

## Unidad 5 — Foros: Genéricos y Colecciones

### Foro recomendado: ¿List, Set o Map para tu problema?

**Objetivo de aprendizaje:** elegir la estructura de datos correcta para un caso real y aplicar genéricos para evitar conversiones y errores de tipo.

**Situación/contexto:** necesitas almacenar en un sistema: (a) los productos en orden de llegada, (b) los DNI únicos de clientes, (c) la relación producto → stock.

**Preguntas guía:**
1. ¿Qué colección elegirías para cada caso y por qué (List, Set, Map)?
2. ¿Qué operaciones (inserción, búsqueda, recorrido) necesitas y qué complejidad esperada tienen?
3. ¿Cómo evita la duplicidad cada estructura?
4. Escribe el código genérico (`List<Producto>`, `Map<String,Integer>`, etc.) y elige un iterador o for-each.

**Consigna de participación:** publicar las 3 decisiones con código y compararlas con las de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Elección de estructura | Correcta y justificada | Aceptable | Incorrecta |
| Genéricos | Usados correctamente | Parcial | Sin genéricos |
| Duplicidad | Bien explicada por estructura | Mencionada | Confusa |
| Recorrido | Correcto y claro | Aceptable | Ausente |
| Interacción | Compara y aporta | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — ArrayList vs LinkedList vs HashMap:** compara las 3 en operaciones típicas (agregar, buscar, eliminar) y decide cuándo usar cada una.
- **Opción 2 — `equals` y `hashCode`:** explica por qué para que un `HashSet` o `HashMap` funcione bien hay que sobreescribir ambos métodos, con un ejemplo concreto.
- **Opción 3 — Interfaz genérica `Caja<T>`:** diseña una clase genérica propia y muestra cómo la usas con dos tipos distintos y qué error de compilación evitas.

---

## Unidad 6 — Foros: E/S y Serialización

### Foro recomendado: ¿Archivo binario, JSON o XML para guardar los datos?

**Objetivo de aprendizaje:** decidir el formato de persistencia adecuado para un caso y aplicar streams de lectura/escritura.

**Situación/contexto:** una app de inventario debe guardar y restaurar sus productos entre ejecuciones.

**Preguntas guía:**
1. ¿Qué formato elegirías (binario con serialización, JSON o XML)? ¿Por qué?
2. ¿Qué ventaja y desventaja tiene cada uno para este caso (tamaño, legibilidad, interoperabilidad)?
3. Escribe el código que serializa/lee una lista de productos con tu formato elegido.
4. ¿Qué pasa si el formato cambia en el futuro? ¿Cómo lo versionarías?

**Consigna de participación:** publicar la decisión + código, y defenderla comparándola con la elección de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Decisión de formato | Justificada | Mencionada | Sin justificar |
| Comparativa | Analiza ventajas y desventajas | Parcial | Ausente |
| Código E/S | Correcto y robusto | Aceptable | Con errores |
| Futuro/versionado | Considerado | Mencionado | Ignorado |
| Interacción | Compara con aporte | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Streams de bytes vs caracteres:** explica la diferencia con ejemplos (leer un `.txt` vs copiar una imagen) y qué clase usarías en cada caso.
- **Opción 2 — Serialización y `serialVersionUID`:** ¿por qué se recomienda declarar `serialVersionUID` en las clases `Serializable`? Cuenta qué pasa si se omite y cambia la clase.
- **Opción 3 — JSON con Jackson:** muestra cómo deserializas una respuesta JSON a un objeto Java con Jackson y qué haces si llega un campo que no conoces.

---

## Unidad 7 — Foros: GUI y Manejo de Eventos

### Foro recomendado: Diseña la interfaz de tu app y su manejo de eventos

**Objetivo de aprendizaje:** aplicar MVC y el modelo de eventos para construir una GUI funcional en JavaFX.

**Situación/contexto:** el cliente pide una pantalla de alta de productos con validación y mensaje de confirmación.

**Preguntas guía:**
1. ¿Qué componentes usas (TextField, ComboBox, Button, TableView) y cómo los organizas (layout)?
2. ¿Cómo separas la lógica de negocio de la vista (MVC)?
3. ¿Qué evento manejas y con qué listener (ej. `ActionEvent`)? Muestra el código.
4. ¿Cómo validas los datos y qué feedback le das al usuario?

**Consigna de participación:** publicar un boceto de la pantalla + el código del manejador de eventos, y sugerir mejoras de usabilidad a un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Componentes/layout | Adecuados y ordenados | Aceptable | Desordenados |
| MVC | Separación clara | Parcial | Todo junto |
| Eventos | Correctos y completos | Parciales | Ausentes |
| Validación | Completa con feedback | Básica | Sin validar |
| Interacción | Sugiere usabilidad | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Modelo de eventos:** explica el ciclo completo de un clic de botón en JavaFX desde el evento hasta el manejador, con un diagrama de texto.
- **Opción 2 — JavaFX vs Swing vs web:** compara las tres opciones para una app de escritorio (curva de aprendizaje, modernidad, mantenimiento) y elige una.
- **Opción 3 — Accesibilidad en GUI:** investiga buenas prácticas de accesibilidad (contraste, navegación por teclado, lectores de pantalla) y aplica 2 a tu pantalla.

---

## Unidad 8 — Foros: Testing y DevOps

### Foro recomendado: ¿Tu código pasa las pruebas de un compañero?

**Objetivo de aprendizaje:** escribir pruebas unitarias con JUnit y configurar un flujo Git/CI que las ejecute automáticamente.

**Situación/contexto:** el equipo decidió que ninguna funcionalidad se acepta sin su test unitario y sin pasar por CI.

**Preguntas guía:**
1. Escribe el test JUnit de un método tuyo (ej. `descuento()` o `validarEmail()`). ¿Qué casos de borde probaste?
2. ¿Qué diferencia pruebas unitarias de pruebas de integración en tu código?
3. ¿Cómo configuras un GitHub Action que ejecute `mvn test` en cada push?
4. ¿Qué beneficios y qué costos ves en exigir tests a todo?

**Consigna de participación:** publicar test + workflow de CI, y ejecutar los tests de un compañero reportando el resultado.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Test JUnit | Casos válidos y de borde | Algunos casos | Triviales |
| Unit vs integración | Correcta | Parcial | Confusa |
| CI workflow | Funcional y documentado | Presente | Ausente |
| Reflexión costo/beneficio | Argumentada | Mencionada | Ausente |
| Interacción | Ejecuta y reporta | Comenta | No comenta |

### Opciones adicionales

- **Opción 1 — Git en equipo:** describe tu flujo de trabajo con Git (ramas, pull requests, merge) y cómo resolverías un conflicto de merge.
- **Opción 2 — Revisión de código:** revisa un fragmento de código (tuyo o de un compañero) y lista 3 mejoras de estilo y 1 error potencial, usando las convenciones vistas.
- **Opción 3 — Javadoc y documentación:** documenta un método de tu código con Javadoc completo y explica por qué documentar bien es parte del trabajo.

---

## Unidad 9 — Foros: Tendencias y Temas Emergentes

### Foro recomendado: ¿Microservicios o monolito para la nueva app?

**Objetivo de aprendizaje:** argumentar la decisión de arquitectura y reconocer cuándo aplicarla, considerando además seguridad y calidad (TDD).

**Situación/contexto:** la empresa quiere lanzar una app de pedidos. Un equipo propone microservicios; otro, un monolito bien estructurado.

**Preguntas guía:**
1. ¿Qué tamaño y equipo tiene la empresa? ¿Cómo afecta esa respuesta?
2. ¿Qué ventajas y desventajas concretas tiene cada opción para este caso?
3. ¿Cómo protegerías la API (validación de entradas, OWASP) y cómo probarías los servicios (TDD, mocks)?
4. ¿Qué recomendarías y qué riesgos asumirías?

**Consigna de participación:** tomar una postura con argumentos técnicos y de contexto, y responder a la postura contraria de un compañero.

**Rúbrica:**

| Criterio | Excelente (10) | Aceptable (7) | Insuficiente (4) |
|---|---|---|---|
| Postura | Clara y argumentada | Presente pero débil | Confusa |
| Contexto | Considera tamaño/equipo | Lo menciona | No lo considera |
| Seguridad/calidad | Incluye OWASP y TDD | Los menciona | Los ignora |
| Postura contraria | La responde con fundamento | La reconoce | La ignora |
| Interacción | Debate constructivo | Comenta | Solo publica |

### Opciones adicionales

- **Opción 1 — Concurrencia vs paralelismo:** con un ejemplo real (descargar archivos, procesar imágenes), explica la diferencia y cómo la resolverías con hilos o `ExecutorService`.
- **Opción 2 — Consumir una API pública:** elige una API pública (JSONPlaceholder, OpenWeatherMap), muestra cómo la consumes con `HttpClient` y cómo probarías la respuesta con un test.
- **Opción 3 — Ética y privacidad:** analiza una app real y lista qué datos recolecta, cuáles son necesarios y cuáles no, y qué dice su política de privacidad según los principios vistos.
