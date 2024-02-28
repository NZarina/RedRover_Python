def add(a, b):
    return a + b


def deduce(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нелья!'