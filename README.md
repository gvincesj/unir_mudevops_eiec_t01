# 📄 Word Sort CLI

Herramienta de línea de comandos desarrollada en Python para procesar listas de palabras desde un archivo de texto o directamente desde la consola.

---

## 🧩 Descripción

`Word Sort CLI` permite leer una colección de palabras y aplicar diferentes operaciones como ordenamiento y eliminación de duplicados.

El programa puede recibir datos desde:

- Un archivo de texto
- Argumentos directamente en la línea de comandos

---

## ⚙️ Requisitos

- Python 3.x

---

## 📂 Formato del archivo

El archivo de entrada debe contener **una palabra por línea**:

```
pera
manzana
banana
pera
uva
```

---

## 🚀 Uso

### 🔹 Sintaxis general

```bash
python main.py [archivo] [opciones]
```

o

```bash
python main.py --file <archivo>
```

---

## 🔧 Parámetros

### 📁 Archivo de entrada

| Parámetro | Descripción |
|----------|------------|
| `<archivo>` | Archivo de texto con palabras (opcional, usa `words.txt` por defecto) |
| `--file` | Especifica archivo de entrada alternativo |

---

### ⚙️ Opciones

| Opción | Descripción |
|-------|------------|
| `--desc` | Ordena las palabras en orden descendente |
| `--unique` | Elimina palabras duplicadas antes de ordenar |

---

## 📌 Ejemplos de uso

### 1. Ordenar palabras (archivo por defecto)

```bash
python main.py
```

### 2. Especificar archivo

```bash
python main.py palabras.txt
```

### 3. Orden descendente

```bash
python main.py palabras.txt --desc
```

### 4. Eliminar duplicados

```bash
python main.py palabras.txt --unique
```

### 5. Combinar opciones

```bash
python main.py palabras.txt --desc --unique
```

### 6. Uso con parámetro `--file`

```bash
python main.py --file palabras.txt
```

### 7. Ingreso directo por consola

```bash
python main.py manzana pera banana
```

---

## 📤 Salida

El programa devuelve una lista ordenada de palabras:

```python
['banana', 'manzana', 'pera', 'uva']
```

---

## ⚠️ Manejo de errores

- Si el archivo no existe:

```
El archivo 'archivo.txt' no existe.
```

- Si el archivo no puede leerse:

```
Error: archivo no encontrado
```

---

## 🏗️ Estructura del programa

- `remove_duplicates()` → elimina duplicados manteniendo el orden  
- `sort_list()` → ordena la lista (ascendente o descendente)  
- `read_file()` → lectura de archivo  

---

## ⚠️ Nota técnica

Actualmente el programa incluye dos enfoques para manejo de argumentos:

- `sys.argv`
- `argparse`

Se recomienda unificar ambos en una sola implementación para evitar conflictos en ejecución.

---

## 📌 Propósito académico

Este proyecto fue desarrollado como parte de una actividad práctica para demostrar:

- Uso de GitHub Flow  
- Trabajo colaborativo con Pull Requests  
- Manejo de ramas y merges  

---

## 👥 Autores

Guillermo Vinces Jara
Fabian Machuca Morán
Isaac Ponce Duarte
Gabriela Vaca Herrera
Nicolle Toala Zurita

