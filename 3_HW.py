#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
# выводим каждое значение отдельно
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])
# все три значения сразу
print(*(my_list[2]))

#3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
numbers = [i for i in list_1 if isinstance(i, (int, float))]
print(sum(numbers))
strings_with_a = [i for i in list_1 if isinstance(i, str) and 'a' in i]
print(strings_with_a)


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
animals = ['cat', 'dog', 'horse', 'cow']
animals_tuple = tuple(animals)
print(animals_tuple)


#3.4. Напишите программу, которая определяет, какая семья больше.
#      1) Программа имеет два input() - например, family_1, family_2.
#      2) Членов семьи нужно перечислить через запятую.
#     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input('Перечислите членов семьи 1 через запятую: ').split(',')
family_2 = input('Перечислите членов семьи  2 через запятую: ').split(',')
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('The first family has more members')
else:
    print('The second family has more members')


#3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию о вашем любимом фильме.
#    - распечатайте только ключи
#    - распечатайте только значения
#    - распечатайте пары ключ - значение

film = {
    'title': "Иван Васильевич меняет профессию",
    'director': 'Гайдай',
    'year': 1973,
    'budget': 'неизвестно',
    'main_actor': 'Юрий Яковлев, Леонид Куравлёв',
    'slogan': 'Танцуют все!!!'
}
print(film.keys())
print(film.values())
print(film.items())


#3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {
    'num1': 375,
    'num2': 567,
    'num3': -37,
    'num4': 21
}
total = sum(my_dictionary.values())
print(total)


#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#option 1
list = [1, 2, 3, 4, 5, 3, 2, 1]
final_list = []
for x in list:
    if x not in final_list:
        final_list.append(x)
print(final_list)

# option 2
print(set(list))


#3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#     - найдите значения, которые встречаются в обоих множествах
#     - найдите значения, которые не встречаются в обоих множествах
#     - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2)) # {1, 100, 5, 9, 'z'}
print(set1.symmetric_difference(set2)) # {'l', 8, 'b', 12, 785, 21, 'a'}
print(set2.issubset(set1)) # False
print(set1.issubset(set2)) # False
