from functools import wraps
import time


# https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit

def logged(func):
    print("Decorating", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called", func.__name__)
        return func(*args, **kwargs)

    return wrapper


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("It takes:", t1 - t0, "seconds")
        return result

    return wrapper
