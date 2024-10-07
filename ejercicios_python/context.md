## Ejercicios sobre Context Manager en Python

### Ejercicio 1: Uso básico de `with` con archivos

Escribe un programa que lea el contenido de un archivo llamado `texto.txt` y lo imprima línea por línea utilizando el bloque `with`.

#### Esqueleto:
```python
with open('texto.txt', 'r') as archivo:
    # Lógica para leer el archivo
    pass
```

### Ejercicio 2: Creación de un Context Manager personalizado

Implementa una clase llamada Temporizador que mida el tiempo que toma ejecutar un bloque de código. Utiliza un Context Manager para ello.

#### Esqueleto:
```python
import time

class Temporizador:
    def __enter__(self):
        # Código para iniciar el temporizador
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Código para finalizar el temporizador y calcular el tiempo transcurrido
        pass

with Temporizador():
    # Bloque de código cuyo tiempo de ejecución será medido
    pass
```


### Ejercicio 3: Suprimir excepciones con __exit__

Modifica el contexto del ejercicio anterior para que suprima las excepciones si el bloque de código genera un ValueError.

#### Esqueleto:
```python

class Temporizador:
    def __enter__(self):
        # Código para iniciar el temporizador
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Lógica para suprimir excepciones de tipo ValueError
        pass

with Temporizador():
    # Lanza una excepción ValueError para probar la supresión
    pass
```
