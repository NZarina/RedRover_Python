# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
import math


def square(a):
    return a * 4, a ** 2, a * (math.sqrt(2))


print(square(4))


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
def person(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


person(name='John', last_name='Smith', age=35, position='web developer')

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
#      создайте новый список, содержащий только положительные числа
my_list = [20, -3, 15, 2, -1, -21]
filtered_list = list(filter(lambda item: item > 0, my_list))
print(filtered_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce

new_list = reduce(lambda num1, num2: num1 * num2, my_list)
print(new_list)

# Чтобы получить результат перемножения только положительных значений
# вариант 1
new_list = reduce(lambda num1, num2: num1 * num2, filtered_list)
print(new_list)
# вариант 2 (вариант преподавателя)
print(reduce(lambda x, y: x * y, [x for x in my_list if x > 0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
import time


def calculate_time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'The {func.__name__} function took {end - start} sec to execute')

    return wrapper


@calculate_time_decorator
def add(a, b):
    time.sleep(2)
    print(a + b)


add(2, 3)

print('-' * 50)


@calculate_time_decorator
def say_hello(name):
    time.sleep(1)
    print(f'Hello, {name}')


say_hello('Zarina')

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические
#      вычисления.
#      Примените эти функции в качестве методов в другом файле.

import my_calc

print(my_calc.add(5, 6))
print(my_calc.deduce (10, 5))
print(my_calc.multiply(5, 5))
print(my_calc.divide(25, 10))
