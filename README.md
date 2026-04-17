# Construcción de Autómata LR(0) — Actividad Práctica 

**Curso:** Compiladores 1  
**Estudiante:** Joel Antonio Jaquez López  
**Carnet:** 23369

---

## Descripción General

Este repositorio contiene la solución a los **dos problemas** de la actividad práctica sobre construcción del autómata LR(0).

---

## Problema 1 — Construcción del Autómata LR(0) (Manual)

**Archivo:** `Problema1/Actividad LR(0).pdf`

Se construyó **manualmente** el autómata LR(0) completo de la gramática:

```
S → S S +
S → S S *
S → a
```

El proceso incluyó:

1. **Gramática aumentada:** Se añadió `S' → S` como símbolo inicial único.
2. **Cálculo de cerradura (Closure):** Para cada conjunto de ítems se calculó la cerradura expandiendo los no-terminales que aparecen después del punto.

---

## Problema 2 — Función CERRADURA con Programa (50%)

**Carpeta:** `Problema2/`  
**Video explicativo:** [https://youtu.be/6wTbHOJaEXs](https://youtu.be/6wTbHOJaEXs)

### ¿Qué es la Cerradura LR(0)?

Un **ítem LR(0)** es una producción con un punto `.` que indica la posición del parser:

```
E' -> . E      ← nada leído aún
E' -> E .      ← ya se leyó E (ítem de reducción / aceptación)
E  -> E . + T  ← se leyó E, falta leer + T
```

La **función Cerradura** expande un conjunto de ítems con esta regla:

> Si el ítem `A → α . B β` está en el conjunto y **B es un no-terminal**,  
> entonces se agregan todos los ítems `B → . γ` para cada producción `B → γ`.  
> Se repite hasta que no se puedan agregar más ítems.

---

### Archivos del Problema 2

| Archivo | Descripción |
|---|---|
| `problema2.py` | Programa principal en Python |
---

### Funciones de `problema2.py`

| Función | Descripción |
|---|---|
| `imprimir_item(item)` | Convierte una tupla `(cabeza, cuerpo, punto)` a texto legible. Ejemplo: `('E', ('E','+','T'), 1)` → `E -> E . + T` |
| `ingresar_gramatica()` | Pide al usuario las producciones de la gramática en formato `A -> sym1 sym2`. Termina con `fin`. |
| `ingresar_items_iniciales()` | Permite ingresar uno o varios ítems del núcleo inicial. Cada ítem se define por su cabeza, cuerpo y posición del punto. Termina con `fin`. |
| `cerradura(items, gramatica)` | Algoritmo principal. Expande el conjunto de ítems aplicando la regla de cerradura y muestra paso a paso cada ítem agregado. |

---

### Cómo ejecutar

```bash
# 1. Entrar a la carpeta
cd "Problema2"

# 2. Crear el entorno virtual (solo la primera vez)
python3 -m venv env

# 3. Activar el entorno
source env/bin/activate

# 4. Correr el programa
python3 problema2.py

# 5. Al terminar
deactivate
```

---

### Gramáticas de prueba

#### Gramática 1 — (Problema 1)

```
S' -> S
S -> S S +
S -> S S *
S -> a
fin
```

**Prueba I0** — ítem inicial `S' -> . S` (punto en posición 0):

```
Símbolo izquierdo: S'     Cuerpo: S     Punto: 0
fin
```

**Salida esperada:**
```
=== CONJUNTO INICIAL ===
  S' -> . S
========================

[Paso 1] Evaluando 'S' en S' -> . S:
  + AGREGADO: S -> . S S +
  + AGREGADO: S -> . S S *
  + AGREGADO: S -> . a

[Paso 1] Evaluando 'S' en S -> . S S +:
 (Ya existe): S -> . S S +
 (Ya existe): S -> . S S *
 (Ya existe): S -> . a

[Paso 1] Evaluando 'S' en S -> . S S *:
 (Ya existe): S -> . S S +
 (Ya existe): S -> . S S *
 (Ya existe): S -> . a

=== CERRADURA FINAL COMPLETA ===
  S' -> . S
  S -> . S S +
  S -> . S S *
  S -> . a
================================
```

**Prueba I1** — núcleo con punto en posición 1 (después de leer `S`):

```
Símbolo izquierdo: S'    Cuerpo: S      Punto: 1
Símbolo izquierdo: S     Cuerpo: S S +  Punto: 1
Símbolo izquierdo: S     Cuerpo: S S *  Punto: 1
fin
```

**Salida esperada:**
```
=== CONJUNTO INICIAL ===
  S' -> S .
  S -> S . S +
  S -> S . S *
========================

[Paso 1] Evaluando 'S' en S -> S . S +:
  + AGREGADO: S -> . S S +
  + AGREGADO: S -> . S S *
  + AGREGADO: S -> . a

[Paso 1] Evaluando 'S' en S -> S . S *:
 (Ya existe): S -> . S S +
 (Ya existe): S -> . S S *
 (Ya existe): S -> . a

[Paso 2] Evaluando 'S' en S -> S . S +:
 (Ya existe): S -> . S S +
 (Ya existe): S -> . S S *
 (Ya existe): S -> . a

[Paso 2] Evaluando 'S' en S -> S . S *:
 (Ya existe): S -> . S S +
 (Ya existe): S -> . S S *
 (Ya existe): S -> . a

=== CERRADURA FINAL COMPLETA ===
  S' -> S .
  S -> S . S +
  S -> S . S *
  S -> . S S +
  S -> . S S *
  S -> . a
================================
```

---

#### Gramática 2 — (vista en clase)

```
E' -> E
E -> E + T
E -> T
T -> T * F
T -> F
F -> ( E )
F -> id
fin
```

**Prueba I0** — ítem inicial `E' -> . E` (punto en posición 0):

```
Símbolo izquierdo: E'    Cuerpo: E    Punto: 0
fin
```

**Salida esperada:**
```
=== CONJUNTO INICIAL ===
  E' -> . E
========================

[Paso 1] Evaluando 'E' en E' -> . E:
  + AGREGADO: E -> . E + T
  + AGREGADO: E -> . T

[Paso 1] Evaluando 'E' en E -> . E + T:
 (Ya existe): E -> . E + T
 (Ya existe): E -> . T

[Paso 1] Evaluando 'T' en E -> . T:
  + AGREGADO: T -> . T * F
  + AGREGADO: T -> . F

[Paso 1] Evaluando 'T' en T -> . T * F:
 (Ya existe): T -> . T * F
 (Ya existe): T -> . F

[Paso 1] Evaluando 'F' en T -> . F:
  + AGREGADO: F -> . ( E )
  + AGREGADO: F -> . id

=== CERRADURA FINAL COMPLETA ===
  E' -> . E
  E -> . E + T
  E -> . T
  T -> . T * F
  T -> . F
  F -> . ( E )
  F -> . id
================================
```

**Prueba I1** — núcleo con punto en posición 1 (después de leer `E`):

```
Símbolo izquierdo: E'    Cuerpo: E      Punto: 1
Símbolo izquierdo: E     Cuerpo: E + T  Punto: 1
fin
```

**Salida esperada:**
```
=== CONJUNTO INICIAL ===
  E' -> E .
  E -> E . + T
========================

=== CERRADURA FINAL COMPLETA ===
  E' -> E .
  E -> E . + T
================================
```

> El punto está seguido de `+` (terminal) → la cerradura no agrega nada nuevo.
