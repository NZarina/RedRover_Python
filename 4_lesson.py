def calc(a, b):
    return a * b
print(calc(3, 4)) # 12. Позиционные параметры


def calc(a, b):
    return a * b
print(calc(b=5, a=2))  # 10. Именованные параметры


def calc(a, b, c=5):
    return a + b + c
print(calc(5, 4, c=10)) # 19, перепишет с на c = 10


def args_function(a, b, *args): # *args - произвольное кол-во позиционных аргументов, вместо args может быть любое слово
    print(a, b, args)
args_function(1, 2, 1, 2, 3) # 1 2 (1, 2, 3)


def kwargs_function(a, b, **kwargs): # **kwargs - произвольное кол-во именованных аргументов, вместо args может быть любое слово
    print(a, b, kwargs)
kwargs_function(1, 2, c=1, d=10) # 1 2 {'c': 1, 'd': 10}


def person(age, f_name, l_name):
    return f'Hello, my name is {f_name} {l_name}. I am {age} y.o.'
print(person(f_name='Zarina', l_name='Niyazova', age=33))
# можем передать аргументы в произвольном порядке, если укажем параметр


def pattern(length, char1, char2):
    return (char1 + char2) * length + char1
print(pattern(8, '*', '-')) # *-*-*-*-*-*-*-*-*


def pattern(length, char1, char2='-'):
    return (char1 + char2) * length + char1
print(pattern(8, '*')) # *-*-*-*-*-*-*-*-*


# SPACE. ПРОСТРАНСТВО ИМЕН
n = 10 # глобальное пространство имен
def mother():
    n = 20 # не локальное пространство имен
    def son():
        n = 30 # локальное пространство имен
        print(n)
    return son
result = mother()
result()
# выведет 30, если не будет n = 30, то выведет 20, если не будет n = 20, то выведет 10


# ЛЯМБДА-ФУНКЦИИ

mult = lambda x, y: x/y
print(mult(5, 6))

l1 = [20, 15, 8, 7, 6]
l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, l))
print(filtered) # -> [20, 18, 48]
print(*filtered) # * - оператор распаковки, распаковывает без скобок -> 20, 18, 48
filtered = list(filter(lambda x: not isinstance(x, str), l))
print(*filtered) # -> 20 15 18 48 40.5

power = list(map(lambda x: x**2, l1))
print(power)

from functools import reduce
result = reduce(lambda x, y: x - y, l1)
print(result)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
