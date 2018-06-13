from time import sleep

from logcall import log_format

logged = log_format('Calling {func.__name__}')


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


def slow_function(s):
    sleep(s)
    return s
