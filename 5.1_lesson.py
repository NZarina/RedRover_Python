class Person:

    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return f'{self.fname}.{self.lname}@gmail.com'


    def hello(self):
        return f'{self.fname} {self.lname} says hello'

    def learn(self):
        return 'I\'m learning'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        print(cls.country)

    @staticmethod
    def is_adult(age):
        return age > 18


class Programmer(Person):
    def __init__(self, fname, lname, language, job_title, salary):
        super().__init__(fname, lname)
        self.language = language
        self._job_title = job_title # weak private indication
        self.__salary = salary # strong private indication

    def coding(self):
        return f'I\'m coding with {self.language}'

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def learn(self): # можно переписать метод родительского класса
        return f'I\'m learning coding'


class Junior(Programmer):
    def __init__(self, fname, lname, language, job_title, age):
        super().__init__(fname, lname, language, job_title)
        self.age = age

class Tester(Person):
    def __init__(self, fname, lname, framework, job_title):
        super().__init__(fname, lname)
        self.framework = framework
        self.job_title = job_title

    def testing(self):
        return f'I\'m testing with {self.framework}'

    def learn(self):
        return f'I\'m learning testing'


print(Person.is_adult(21))
person_1 = Person('Alex', 'Baker')
print(person_1.email)
person_1.fname = 'Bob'
print(person_1.fname)
print(person_1.email)
print(person_1.__dict__)
print(person_1.lname)
print(person_1.fname)
person_1.fname = 'Alexander'
print(person_1.__dict__)
print(person_1.hello())
print(person_1.country)
print(person_1.fname)
print(person_1.__dict__)
print(person_1.learn())



#
person_2 = Person('Kevin', 'Smith')
print(person_2.lname)
print(person_2.fname)
print(person_2.__dict__)
print(person_2.hello())
#
coder_1 = Programmer('Alejandro', 'Villarel', 'Python', 'Senior developer', 10000)
print(coder_1.lname)
print(coder_1.language)
print(coder_1.job_title)
print(coder_1.coding())
print(coder_1.country)
print(coder_1.get_salary())
print(coder_1.set_salary(20000))
print(coder_1.get_salary())
print(coder_1._Programmer__salary)
print(coder_1._job_title)
print(coder_1.learn())
tester_1 = Tester('pytest', 'SDET', fname='Leonardo')
print(tester_1.country)
tester_1.change_country('Canada')
print(tester_1.fname)
print(tester_1.framework)
print(tester_1.testing())
print(tester_1.country)
print(tester_1.learn())