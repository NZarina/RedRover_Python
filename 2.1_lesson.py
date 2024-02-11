s = 'hello world'

# метод replace() заменяет элементы
# print(s.replace('e', 'a')) # заменит "е" на "а" -> hallo world
# print(s.replace('l', '?', 2)) # заменит первые две "l" на "?" -> he??o world
#
# # метод count() подсчитывает кол-во элементов в строке
# print(s.count('o')) # подсчитает кол-во "о" -> 2
#
# # метод split() разделяет строку на список подстрок по разделителю
# name = 'Иванов Иван Иванович'
# numbers = '1, 2, 3, 4, 5'
# print(name.split()) #преобразует в список и разделит пробелами -> ['Иванов', 'Иван', 'Иванович']
# print(name.split('а')) #разделит по букве "а" -> ['Ив', 'нов Ив', 'н Ив', 'нович']
# print(numbers.split(',')) #-> ['1', ' 2', ' 3', ' 4', ' 5']
# print(numbers.split(',', maxsplit=2)) #-> ['1', ' 2', ' 3, 4, 5']

# метод join
# print(''.join(numbers))

# метод strip вернет копию строки str с удаленными начальными и конечными символами chars
# w3 = '     hello     '
# print(w3)
# print(w3.strip()) #-> hello (без пробелов)
#
# w3 = '123hello123'
# print(w3)
# print(w3.strip('123')) #-> hello (без 123)
#
# w3 = '   123hello123   '
# print(w3)
# print(w3.strip().strip('123')) #-> hello (без пробелов и 123)

# find() для поиска в строке. В качестве обязательного аргумента принимает строку,
# которую нужно найти. Метод возвращает индекс символа, с которого начинается искомая строка.
# Если строка не найдена, метод вернет -1.
# w4 = 'hello world'
# print(w4.find('e')) #-> 1
# print(w4.find('o',2, 5))  #-> 4

#
# w5 = 'tyPe YOUR name'
#
# # upper() для перевода в верхний регистр
# print(w5.upper()) #-> TYPE YOUR NAME
#
# # lower() для перевод в нижний регистр
# print(w5.lower()) #-> type your name
#
# # title() все первые буквы будут в верхнем регистре, остальные - в нижнем
# print(w5.title()) #-> Type Your Name
#
# # capitalize() первый символ в верхнем регистре, остальные -  в нижнем регистре.
# print(w5.capitalize()) #-> Type your name
#
# #swapcase - Возвращает копию строки, в которой каждая буква будет иметь противоположный регистр.
# print(w5.swapcase()) #-> TYpE your NAME

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = 'QWERTY'
# print(w6.islower()) #-> True
# print(w7.islower()) #-> False
# print(w6.isupper()) #-> False
# print(w8.isupper()) #-> True

# метод isdigit() возвращает True , если все символы в строке str являются цифрами и есть хотя бы один символ

# метод isalpha() возвращает True, если все символы в строке str являются буквенными и есть хотя бы один символ
