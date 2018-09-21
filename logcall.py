from functools import wraps
import time
import csv

'''
Define un decorator llamado: instrumented
debe aceptar como parámetro el path del archivo csv donde va a escribir
usa la funcion send_to_csv para guardar las métricas de la función

>>> from sample import slow_function
>>> slow_function(5)
It takes 5 seconds

abre el archivo time_series_log.csv para verificar el registro
'''


def send_to_csv(func_name, ts, duration, path):
    """
    Writes a record in csv file
    :param path: csv path
    :param func_name: the function name
    :param ts: timestamp
    :param duration: duration in seconds
    :return: None
    """
    with open(path, mode='a') as csv_file:
        row = {"function_id": func_name, "time_stamp": ts, "duration": duration}
        writer = csv.DictWriter(csv_file, fieldnames=row.keys())
        writer.writerow(row)


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


def instrumented(path):
    def time_it(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            t1 = time.time()
            duration = t1 - t0
            send_to_csv(func.__name__, t0, duration, path)
            print("It takes:", duration, "seconds")
            return result

        return wrapper

    return time_it


def log_methods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            # is a method?
            setattr(cls, key, logged(value))
    return cls
