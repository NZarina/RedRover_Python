# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
# - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
#     нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

class Vehicle:
    def __init__(self, make, color, year, price):
        self.make = make
        self.color = color
        self.year = year
        # self.price = price
        self._price = price #private

    def short_info(self):
        return f'Make and model: {self.make}. Price: {self._price}'

    def get_price(self):
        return f'The price is {self._price}'

    def set_price(self, new_price):
        self._price = new_price

Car1 = Vehicle('Audi a4', 'red', 2015, '10K USD')
# print(Car1.make)
# print(Car1.short_info())
# print(Car1.price)
# Car1.price = '15'
# print(Car1.price)
# Car1._price = '30K'
# print(Car1._price)
Car1.set_price('25K USD')
print(Car1.get_price())

Car2 = Vehicle('BMW x5', 'black', 2020, '20K USD')

class Lorry(Vehicle):
    def __init__(self, make, color, year, price, new_used):
        super().__init__(make, color, year, price)
        self.new_used = new_used


    def short_info(self):
        return f'Make and model: {self.make}. Price: {self._price}'


    def short_info_added(self):
        return f'Make and model: {self.make}. Price: {self._price}. State: {self.new_used}'

Car3 = Lorry('unknown', 'green', 2017, '18L USD', 'new')
# print(Car3.short_info())
print(Car3.short_info_added())
print(Car3.short_info_added())