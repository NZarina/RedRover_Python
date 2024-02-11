# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# import math
#
# def square(a):
#     return a*4, a**2, a*(math.sqrt(2))

# print(square(4))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def person(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# person(name='John', last_name='Smith', age=35, position='web developer')



# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# filtered_list = list(filter(lambda item: item > 0, my_list))
#
# print(filtered_list)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# new_list = reduce(lambda num1, num2: num1*num2, my_list)
# print(new_list)
#
# new_list = reduce(lambda num1, num2: num1*num2, filtered_list)
# print(new_list)
# print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0])) #вариант преподавателя

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time

# def count_execution_time(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         end = time.perf_counter()
#         exec_time = end - start
#         print(f'{func.__name__} execution time is: {exec_time}')
#         return result
#     return wrapper
#
# @count_execution_time
# def greeting(name):
#     return f'Hello {name}!'
#
# greeting('Zarina')
# print(greeting('Zarina'))


import time

def greeting(name):
    return f'Hello {name}!'


def execution_time(time):
    start = time.perf_counter()
    greeting('Zarina')
    end = time.perf_counter()
    result = end - start
    print(result)
    return result



print(greeting('Zarina'))



# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# import my_calc
# print(f'Addition result is: {my_calc.addition(5,6)}')
# print(my_calc.deduction(10, 5))
# print(my_calc.multiplication(5,5))
# print(my_calc.division(25, 10))



