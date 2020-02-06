# Слоты

class MyClass:

    def __init__(self):
        self.a = 1


m = MyClass()
m.b = 100
print(m.b)

m.f = lambda x: x ** 2

print(m.f(2))

print(m.__dict__)

print(m.a)

print(m.__dict__['a'])


# n = MyClass()
# print(n.b)

class MySlotClass:
    __slots__ = ('a', 'b')

    def __init__(self):
        self.a = 1

    def f(self):
        pass


m = MySlotClass()
m.a = 1
m.b = 2
print(m.a, m.b)

# m.z = 100
# print(m.z)

# print(m.__dict__)

m.b = lambda x: x**2