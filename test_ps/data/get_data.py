import os

FILEPATH = os.path.dirname(os.path.abspath(__file__))


def get_simple_csv():
    return os.path.join(FILEPATH, "simple.csv")


def get_simple_csv2():
    return os.path.join(FILEPATH, "simple2.csv")


def get_simple_csv3():
    return os.path.join(FILEPATH, "simple3.csv")