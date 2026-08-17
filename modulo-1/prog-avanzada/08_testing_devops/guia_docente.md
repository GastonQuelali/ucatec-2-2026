# GUÍA DOCENTE — Unidad 9: Pruebas, Buenas Prácticas y DevOps Básico

**Autor:** Ing. Gaston Genaro Quelali Calcina
**Materia:** Programación Avanzada (SIS120) · **Nivel:** Universitario
**Tiempo estimado:** 2 clases de 80 minutos (teoría + práctica)
**Material de apoyo:** `teoria.md` · `presentacion.md` · diagramas `assets/mermaid/`

---

## 1. Objetivos de aprendizaje

Al finalizar la unidad, el estudiante podrá:

1. **Escribir** pruebas unitarias con JUnit 5 siguiendo el patrón AAA.
2. **Documentar** el código con JavaDoc y aplicar convenciones de estilo.
3. **Usar** Git con ramas, Pull Requests y colaboración en GitHub.
4. **Configurar** un pipeline CI/CD básico con GitHub Actions.

---

## 2. Plan de clases

### Clase 1 — Testing y documentación (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Disparador: *"¿Cómo sabes que tu código sigue funcionando?"* | Debate guiado |
| 20' | Testing: unitarias vs integración | Slides 3-4 |
| 25' | JUnit 5 y patrón AAA | Slides 5-7 |
| 20' | JavaDoc y convenciones | Slides 8-9 |
| 5' | Cierre | — |

### Clase 2 — Git, CI/CD y práctica (80 min)

| Tiempo | Actividad | Recurso |
|---|---|---|
| 10' | Git: ramas y flujo de trabajo | Slides 10-12 |
| 15' | Colaboración con Pull Requests | Slide 13 |
| 15' | CI/CD y GitHub Actions | Slides 14-15 |
| 35' | **Taller**: tests + pipeline CI | Guía práctica (abajo) |
| 5' | Cierre | — |

---

## 3. Taller práctico (guía para el alumno)

1. En el proyecto de la Unidad 7 (catálogo), agregar **JUnit** y escribir tests para:
   - `descuento(precio)` que aplica 10%.
   - `retirar()` con saldo suficiente e insuficiente.
2. Documentar las clases con **JavaDoc** y aplicar convenciones de estilo.
3. Crear una rama `feature/tests`, hacer commits, push y abrir un **Pull Request**.
4. Configurar `.github/workflows/ci.yml` para compilar y probar en cada push.
5. **Reto extra:** corregir un test que falle a propósito y verificar que el pipeline lo detecta.

**Criterios de evaluación:**
- Tests JUnit correctos y con nombres descriptivos.
- JavaDoc en clases y métodos públicos.
- Pull Request con revisión de pares.
- Pipeline CI que pasa/falla según el estado real del código.

---

## 4. Evaluación

- **Taller práctico (50%):** tests + pipeline CI funcional.
- **Evaluación formativa (20%):** preguntas orales.
- **Prueba escrita (30%):** JUnit, Git, CI/CD.

---

## 5. Material didáctico

- `presentacion.md` — slides para clase (Marp).
- `assets/mermaid/01_flujo_testing.mmd` — flujo de pruebas.
- `assets/mermaid/02_git_workflow.mmd` — flujo Git con ramas.
- `assets/mermaid/03_pipeline_cicd.mmd` — pipeline CI/CD.
- `assets/mermaid/04_junit.mmd` — relación clase-test.
- `assets/mermaid/05_documentacion_estilo.mmd` — documentación y estilo.

---

## 6. Recursos complementarios

- JUnit 5 — *User Guide* (junit.org).
- Git — *Pro Git Book* (git-scm.com/book).
- GitHub Docs — *About CI*, *About Pull Requests*.
- Google Java Style Guide.
