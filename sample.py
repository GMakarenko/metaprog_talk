from logcall import logged, time_it
from time import sleep


@logged
def add(x, y):
    """
    Adds x and y
    :param x: a number
    :param y: a number
    :return:
    """
    return x + y


@logged
def sub(x, y):
    return x - y


@logged
def mul(x, y):
    return x * y


@time_it
def slow_function(s):
    """
    Simula una funcion que tarda s segundos en ejecutarse
    :param s:
    :return:
    """
    sleep(s)
    return None
