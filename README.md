# I Decorators

## Introduccion: Como funcionan los argumentos en Python

* Explicar los parametros \*args y \*\*kwargs
* Hacer un wrapper sencillo

## Basic decorator

* Ir a decorators\_1
* Hacer el decorator para logs y mostrar como decorar una funcion manualmente

```python
# logcall.py
# from functools import wraps

def logged(func):
    print("Decorating", func.__name__) # Ponemos este print para que vean cuando se aplica el decorator
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called", func.__name__)
        return func(*args, **kwargs)

    return wrapper
```

```python
from logcall import logged

def add(x, y):
	return x + y

add = logged(add)
```

```python
from logcall import logged

@logged
def add(x, y):
	return x + y
```

* Explicar el signature de la función


```python
# logcall.py
from functools import wraps

def logged(func):
    print("Decorating", func.__name__) # Ponemos este print para que vean cuando se aplica el decorator

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called", func.__name__)
        return func(*args, **kwargs)

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__

    return wrapper
```

 * Mandar a decorators\_2 y dejar el ejercicio de time\_it (La solución está en logcall.py \[decorators\_3\])
 * Checar la solución en grupo

## Decoretors with params

* Preguntar que se tendría que hacer para que un decorator acepte parametros

```python
# logcall.py

def log_with_param(param):
	"""
    Esta funcion regresa un decorator 
    """
    def logged(func):
        print("Decorating", func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(param)
            return func(*args, **kwargs)

        return wrapper

    return logged
```

```python
# sample.py

@log_with_param(">>> This is a test")
def add(x, y):
    """
    Adds x and y
    :param x: a number
    :param y: a number
    :return:
    """
    return x + y
```

* Explicar como funcionan los decorators con parámetros en shell

```python
# shell
def add(x, y):
	return x + y

from logcall import log_with_param

decorate = log_with_param("This is a test")

add = decorate(add)

add(5,8)
```

* Mostrar algunos ejemplos (Flask, etc), que usan decorators con parametros.

* Mandar a decorators\_4 y dejar el ejercicio de instrumented (La solución está en logcall.py \[decorators\_5\])

* Checar la solución en grupo

## Class decorators

* Explicar ejemplo sencillo en shell

```python
def decorate(cls):
	print("Decorating", cls)
	return cls

@decorate
class X:
	def hey(self):
		print("Hey!")
```

* Explicar el decorator log\_methods y MyClass

```python
# logcall.py

def log_methods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            # is a method?
            setattr(cls, key, logged(value))
    return cls

```

```python
# sample.py

@log_methods
class MyClass:
    def __init__(self, value):
        self.value = value

    def hey(self):
        print("Hey")

    def you(self):
        print("you")

```

* Se podría profundizar en este tema y dejar un ejercicio o explicacion adicional

# II Meta-classes

* Dar la introducción de type

```python
# shell

x = 5
y = 1.3
z = "asdf"
type(x)
type(y)
type(z)

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

p = Point(2, 3)
type(p)

# Mind blowing here
int
float
Point
str
type(int)
type(float)
type(Point)
type(str)

# More mind blowing
type

```

* Dar la introducción de como se definen las clases

Una clase se compone de 3 cosas:

name

bases = (object,) por si hay multi-herencia

methods = {'method_name': method}

type define clases con estos elementos, esto es lo que pasa cuando escribimos class Point...

```python
Point  = type(name, bases, methods)
p = Point(2,3)
p.x
p.y
p.move(1, 5)

```

Si type es la clase que se encarga de construir tipos, qué pasa si quiero hacer mi popia clase para construir tipos?

```python
class MyType(type):
	def __new__(meta, clsname, bases, methods):
		print('Creating', clsname)
		print('Bases', bases)
		print('Methods', list(methods))
		return super().__new__(meta, clsname, bases, methods)

Point = MyType(name, bases, methods)
Creating ...
Bases ...
Methods ...

p = Point(2,3)
p.x
p.y
p.move(1, 5)
```

Otra forma de decirle a python con que type queremos que defina nuestra clase es utilizando *metaclass*

```python
class Point(metaclass=mytype):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

Creating ...
Bases ...
Methods ...

```

Observar que no se ha instanciado la clase, solo se interceptó su definición. Todas las clases que hereden de una clase definida con una metaclase tendran este comportamiento. 

# to be continued...
