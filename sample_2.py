from logcall import log_format

logged = log_format("Calling: {func.__name__} from sample_2.py ")


@logged
def div(x, y):
    return x / y
