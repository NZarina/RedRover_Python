# Вариант 1 для создания списков
my_list = [1, 'hello', 2.0, True, None]
#
# # Вариант 2 для создания списков
sentence = 'Python is awesome!'
# print(sentence.split(' ')) # -> ['Python', 'is', 'awesome!']
# print(sentence.split(' ', maxsplit=1)) # -> разделить до первого пробела ['Python', 'is awesome!']

# Работа с элементами списка
# my_list = [1, 'hello', 2.0, True, None]
# print(my_list)
# print(id(my_list))
# # print(my_list[0])  # -> 1
# # print(my_list[-1])  # -> None
# my_list[0] = 25
# print(my_list)
# print(id(my_list))

# print(my_list)
# # my_list.append(sentence) # -> добавляет в конец списка
# # print(my_list) # -> [1, 'hello', 2.0, True, None, 'Python is awesome!']
# my_list.insert(0, sentence)
# print(my_list) # -> ['Python is awesome!', 1, 'hello', 2.0, True, None, 'Python is awesome!']
# # print(len(my_list)) # -> узнать длину списка

# print(my_list.count(1)) # -> 2 (выведет кол-во элементов со значением 1)

# print(my_list.index(1)) # -> 0 (метод ищет элемент в списке и возвращает его индекс)

my_list = [1, 2, 3, 4, 5], [6, 7]
# print(sum(my_list)) # -> 15 (сумма всех элементов в списке)
# print(min(my_list)) # -> 1
# print(max(my_list)) # -> 5

# my_list1 = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, [11, 12, 13, 14]]]
# # print(my_list1[-1][-1][0])
# # my_list1.reverse() # -> 15 [[6, 7, 8, 9, 10, [11, 12, 13, 14]], 5, 4, 3, 2, 1]
# # print(my_list1)
#
# numbers = [1, 2, 3, 4, 5]
# new_l = [i*i for i in numbers if i%2==0] # -> [4, 16]
# print(new_l)

# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)
#
# letters = list(my_tuple) #переобразовали в список
# letters[0] = 'ananas'
# print(letters)


