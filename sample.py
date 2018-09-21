from time import sleep

from logcall import logged, log_with_param, instrumented, log_methods


@log_with_param(">>> This is a test")
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


@instrumented('time_series_log.csv')
def slow_function(s):
    """
    Simula una funcion que tarda s segundos en ejecutarse
    :param s:
    :return:
    """
    sleep(s)
    return None


@log_methods
class MyClass:
    def __init__(self, value):
        self.value = value

    def hey(self):
        print("Hey")

    def you(self):
        print("you")
