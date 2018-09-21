from functools import wraps

'''
Utiliza la solución de está pregunta:

https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit

Y haz un decorator que se llame time_it que mida el tiempo de ejecución y lo imprima

>>> from sample import slow_function
>>> slow_function(5)
It takes 5 seconds
>>>

'''


def logged(func):
    print("Decorating", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called", func.__name__)
        return func(*args, **kwargs)

    return wrapper
