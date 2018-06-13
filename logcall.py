from functools import wraps


def logged(func):
    print("Decorating", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called", func.__name__)
        return func(*args, **kwargs)

    return wrapper
