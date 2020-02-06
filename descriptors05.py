# Дескрипторы


class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val < 0:
            raise ValueError('Возраст не может быть отрицательным')
        self._age = val


class Salary:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError('Значение не может быть отрицательным')
        self._value = val


person = Person(10)

person.age = 20

# person.age = -10

salary = Salary(100)

salary.value = 10
# salary.value = -10
