from sqlalchemy import Column


# Column

# Дескрипторы
class PositiveIntegerField:

    def __init__(self, val=0):
        if val < 0:
            raise ValueError('Значение не может быть отрицательным')
        self._val = val

    def __get__(self, instance, owner):
        print('Сработал get дескриптора')
        return self._val

    def __set__(self, instance, value):
        print('Сработал set дескриптора')
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        self._val = value

    def __delete__(self, instance):
        del self._val


class SmallPositiveIntegerField(PositiveIntegerField):

    def __set__(self, instance, value):
        if value > 100:
            raise Exception('Слишком большое число')
        super().__set__(instance, value)


class Person:
    # Свойства дескрипторы объявляются внутри класса
    age = SmallPositiveIntegerField(1)
    count = PositiveIntegerField()

    def __init__(self, age):
        self.age = age


class Salary:
    value = PositiveIntegerField(1)

    def __init__(self, value):
        self.value = value


person = Person(1)

person.age = 200
print(person.age)

del person.age

# person.age = -10

salary = Salary(100)

salary.value = 10
