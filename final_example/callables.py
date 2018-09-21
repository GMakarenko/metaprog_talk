from time import sleep

from logcall import instrumented


@instrumented('time_series_log.csv')
def function_1(s):
    sleep(s)
    return None


@instrumented('time_series_log.csv')
def function_2(s):
    sleep(s)
    return None


@instrumented('time_series_log.csv')
def function_3(s):
    sleep(s)
    return None
