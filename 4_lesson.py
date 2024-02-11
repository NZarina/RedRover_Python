# def calc(a, b):
#     return a * b
#
# print(calc(3, 4))
#
#
# def calc(a, b):
#     return a * b
#
# print(calc(b=5, a=2))
#
#
# def calc(a, b):
#     return a * b
#
# print(calc(b=5, a=2))
#
# def person(age, f_name, l_name='Niyazova'):
# # def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} y.o.'
#
# print(person(33, 'Zarina', 'Niyazova'))
# print(person(f_name='Zarina', l_name='Niyazova', age=33))

# print(sum([5, 6, 7])) #сумма чисел
# print(min([5, 6, 7]))
# print(max([5, 6, 7]))

# def pattern(length, char1, char2):
#     return (char1 + char2) * length + char1
#
# print(pattern(8, '*', '-')) #*-*-*-*-*-*-*-*-*
#
#
# def pattern(length, char1, char2='-'):
#     return (char1 + char2) * length + char1
#
# print(pattern(8, '*')) #*-*-*-*-*-*-*-*-*

# mult = lambda x, y: x/y
# print(mult(5, 6))

l1 = [20, 15, 8, 7, 6]
l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, l))
# print(filtered) # -> [20, 18, 48]
# print(*filtered) # * - оператор распаковки, распаковывает без скобок -> 20, 18, 48
# filtered = list(filter(lambda x: not isinstance(x, str), l))
# print(*filtered) # -> 20 15 18 48 40.5
#
# power = list(map(lambda x: x**2, l1))
# print(power)

# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
# print(result)

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


