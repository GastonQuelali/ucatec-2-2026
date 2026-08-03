---
marp: true
theme: default
paginate: true
header: "Unidad 1 — Introducción a los Sistemas ERP"
footer: "UCatec · Informática"
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
---

<!-- _class: title -->

# Sistemas ERP
## Planificación de Recursos Empresariales
### Unidad 1 · Introducción

---

## Agenda

1. **¿Qué es un ERP?** — definición, historia, objetivos, características
2. **Componentes** — arquitectura y módulos
3. **1.1 Usos y aplicaciones**
4. **1.2 Tipos de ERP** — despliegue, alcance, licencia, comparativa
5. **1.3 Inserción de usuarios y empresas** — conceptos y práctica en Odoo

---

## ¿Qué es un ERP?

> **ERP** = *Enterprise Resource Planning*
> **Planificación de Recursos Empresariales**

Sistema de gestión **integrado** que administra los procesos de la empresa con una **única base de datos** y **módulos** compartidos.

| Letra | Palabra | Idea |
|---|---|---|
| **E** | Enterprise | Empresa |
| **R** | Resource | Recursos |
| **P** | Planning | Planificación |

**Sin ERP:** cada área lleva "su" información por separado. **Con ERP:** una sola fuente de verdad.

---

## Evolución histórica

```mermaid
timeline
    title Evolución de los ERP
    1960s-70s : MRP – materiales para producción
    1980s : MRP II – producción + máquinas + mano de obra
    1990s : ERP – integra toda la empresa (Gartner)
    2000s : ERP II – internet, CRM, SCM
    2010s+ : Cloud ERP – SaaS, actualizaciones automáticas
```

---

## Objetivos fundamentales

- **Integrar** todos los procesos y áreas en un solo sistema
- **Unificar** la información (una sola fuente de verdad)
- **Automatizar** tareas repetitivas y reducir errores
- **Dar visión global** en tiempo real de la organización
- **Estandarizar** los procedimientos
- **Soportar decisiones** con datos confiables

---

## Características esenciales

| Característica | Descripción |
|---|---|
| **Modularidad** | Módulos según el área funcional |
| **BD centralizada** | Todos usan la misma base de datos |
| **Integración** | Un proceso dispara los siguientes |
| **Parametrización** | Se configura, no se reprograma |
| **Multiusuario** | Muchos usuarios simultáneos con permisos |
| **Multientidad** | Varias empresas en un sistema |
| **Escalable** | Crece junto a la empresa |

---

## Arquitectura en 3 capas

```mermaid
flowchart TB
    subgraph P["Capa de Presentación"]
        A1["Interfaz de usuario<br/>(navegador / app)"]
    end
    subgraph A["Capa de Aplicación"]
        B1["Módulos de negocio"]
        B2["Reglas de negocio"]
        B3["Usuarios, roles, permisos"]
    end
    subgraph D["Capa de Datos"]
        C1["Base de datos centralizada<br/>(PostgreSQL, Oracle…)"]
    end
    A1 --> B1
    B1 --> B2
    B1 --> C1
    B2 --> C1
    B3 --> C1
```

> ⚠️ La capa de datos es una **base de datos relacional** → tema de las Unidades 2 a 6.

---

## Módulos típicos de un ERP

```mermaid
flowchart LR
    CENTRO["BASE DE DATOS CENTRALIZADA"]
    FIN["Finanzas y Contabilidad"]
    VTA["Ventas / CRM"]
    CMP["Compras"]
    INV["Inventario / Logística"]
    PRO["Producción / MRP"]
    RHS["RRHH y Nómina"]
    PRJ["Proyectos"]
    BI["Reportes / BI"]
    FIN --- CENTRO
    VTA --- CENTRO
    CMP --- CENTRO
    INV --- CENTRO
    PRO --- CENTRO
    RHS --- CENTRO
    PRJ --- CENTRO
    BI --- CENTRO
```

---

## Flujo de datos integrado — Una venta

```mermaid
flowchart LR
    A["Venta de 100 u."] --> B["Verifica stock"]
    B --> C["Descuenta stock"]
    C --> D["Factura"]
    C --> E["Orden de fabricación si falta"]
    E --> F["Orden de compra a proveedor"]
    D --> G["Reportes actualizados"]
    C --> G
```

**Un solo registro alimenta todos los módulos.** Sin re-tipear nada.

---

## Beneficios y desafíos

<div class="columns">
<div>

**✅ Beneficios**
- Información única y en tiempo real
- Menos errores y duplicación
- Automatización de procesos
- Reducción de costos
- Trazabilidad y auditoría
- Reportes para decidir

</div>
<div>

**⚠️ Desafíos**
- Costo de licencias e implementación
- Implementación larga y compleja
- Resistencia al cambio
- Reingeniería de procesos
- Dependencia del proveedor

</div>
</div>

---

## 1.1 Usos por área funcional

| Área | Uso típico |
|---|---|
| Dirección | Tableros de control, KPI, presupuestos |
| Ventas / Marketing | CRM, pedidos, cotizaciones, comisiones |
| Compras | Órdenes de compra, evaluación de proveedores |
| Producción | Fabricación, listas de materiales, calidad |
| Logística | Stock, trazabilidad, traslados |
| Finanzas | Contabilidad, facturación, cobranzas, impuestos |
| RRHH | Legajos, asistencia, sueldos |
| Administración | Empresas, usuarios, roles, permisos |

---

## 1.1 Aplicaciones por sector

```mermaid
mindmap
  root((Sectores))
    Industrial
      Producción y MRP
      Control de calidad
    Retail
      Punto de venta
      Inventario multicanal
    Servicios
      Facturación por horas
      Proyectos
    Salud
      Pacientes
      Stock de insumos
    Construcción
      Presupuesto de obra
      Avance de obra
    Educación
      Inscripciones
      Aranceles
```

---

## 1.2 Tipos de ERP

```mermaid
flowchart TD
    ROOT["TIPOS DE ERP"]
    ROOT --> DEP["Según despliegue"]
    ROOT --> ALC["Según alcance"]
    ROOT --> LIC["Según licencia"]
    DEP --> ONP["On-premise"]
    DEP --> CLOUD["Cloud / SaaS"]
    DEP --> HIB["Híbrido"]
    ALC --> HOR["Horizontal"]
    ALC --> VER["Vertical"]
    LIC --> PRO["Propietario"]
    LIC --> LIB["Open Source"]
```

---

## 1.2 Despliegue: on-premise vs cloud

| Criterio | On-premise | Cloud / SaaS |
|---|---|---|
| Instalación | Servidores propios | Servidores del proveedor |
| Pago | Licencia inicial alta | Suscripción mensual |
| Acceso | Red interna | Cualquier lugar, internet |
| Actualizaciones | Manuales | Automáticas |
| Costo inicial | **Alto** | **Bajo** |
| Control de datos | Total | Del proveedor |

**Tendencia actual:** migración hacia la nube.

---

## 1.2 Comparativa de productos

| | SAP S/4HANA | Oracle Cloud | Dynamics 365 | Odoo | ERPNext |
|---|---|---|---|---|---|
| Tipo | Propietario | Propietario | Propietario | Open source | Open source |
| Empresa | Grande | Grande | Grande/Media | PYME/Grande | PYME |
| Costo | Muy alto | Alto | Alto | Gratis (community) | Gratis (self-hosted) |
| Dificultad | Alta | Alta | Media | Baja | Baja |

> **En la materia usaremos Odoo** por ser gratuito, fácil y completo para práctica.

---

## 1.2 Criterios de selección

```mermaid
flowchart LR
    A["1. Necesidades"] --> B["2. Presupuesto"]
    B --> C["3. Despliegue (nube/local)"]
    C --> D["4. Tamaño de empresa"]
    D --> E["5. Funcionalidad por industria"]
    E --> F["6. Licencias y soporte"]
    F --> G["7. Facilidad de uso"]
    G --> H["Decisión"]
```

---

## 1.3 Conceptos clave

| Concepto | Definición |
|---|---|
| **Empresa (tenant)** | Organización administrada dentro del ERP |
| **Usuario** | Persona con login y contraseña |
| **Rol / Grupo de acceso** | Conjunto de permisos asignados |
| **Permiso** | Derecho: ver, crear, modificar, eliminar |
| **Autenticación** | ¿Quién sos? (identidad) |
| **Autorización** | ¿Qué podés hacer? (permisos) |

> **Clave:** autenticación ≠ autorización.

---

## 1.3 Estructura multientidad

```mermaid
flowchart TB
    ERP["ERP (una instalación)"]
    EMP1["Empresa A"]
    EMP2["Empresa B"]
    EMP3["Empresa C"]
    ERP --> EMP1
    ERP --> EMP2
    ERP --> EMP3
    EMP1 --> U1["Usuario: Admin"]
    EMP1 --> U2["Usuario: Vendedor"]
    EMP2 --> U4["Usuario: Comprador"]
```

- Varias empresas, una sola instalación
- Datos **aislados** entre empresas
- Un usuario puede tener roles distintos en cada empresa

---

## 1.3 Seguridad por roles (RBAC)

```mermaid
flowchart LR
    U["Usuario"] --> R2["ROL Vendedor"]
    U --> R3["ROL Contador"]
    U --> R1["ROL Administrador"]
    R1 --> P1["✓ Todo: usuarios, empresas, módulos"]
    R2 --> P2["✓ Pedidos, catálogo<br/>✗ Contabilidad, costos"]
    R3 --> P3["✓ Facturas, reportes<br/>✗ Pedidos"]
```

**RBAC:** el usuario recibe **roles**, no permisos sueltos → mínimo privilegio, fácil auditoría.

---

## 1.3 Práctica con Odoo

1. **Crear empresa:** Ajustes → Compañías → Crear
2. **Crear usuario:** Ajustes → Usuarios → Crear (nombre, correo, contraseña)
3. **Asignar permisos:** por módulo elijo nivel de acceso
   - Sin acceso / Solo lectura / Operaciones propias / Todas / Administrador
4. **Verificar:** iniciar sesión como el usuario nuevo y comprobar qué ve y qué no

| Usuario | Ventas | Inventario | Contabilidad | Ajustes |
|---|---|---|---|---|
| Ana (vendedora) | Operaciones | Lectura | Sin acceso | Sin acceso |
| Juan (contador) | Lectura | Lectura | Operaciones | Sin acceso |

---

## Repaso rápido

1. ¿Qué significa ERP?
2. ¿MRP → MRP II → ERP → ERP II → Cloud? Contá la evolución
3. ¿Autenticación vs autorización?
4. ¿Qué es un tenant?
5. ¿Qué es RBAC?
6. ¿Cómo creo un usuario en Odoo?

**Práctica:** crear 3 usuarios (vendedor, contador, comprador) en Odoo y verificar sus accesos.

---

<!-- _class: title -->
# ¡Gracias!
### Dudas y consultas
