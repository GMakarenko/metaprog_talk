from logcall import logged


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
