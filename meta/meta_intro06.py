# Все в питоне является объектом


class MyClass:
    pass


m = MyClass()

n = 1

print(type(n))
print(n.__class__)


def f():
    pass


print(f)
print(type(f))

print(f.__class__)


# MyClass - тоже объект (класс - это тоже объект!)

def fcls(cls):
    cls.a = 100


fcls(MyClass)

print(MyClass.a)

# Класс MyClass создает оъект m
m = MyClass()

# Объект m создал класс MyClass
# Т.к. класс тоже объект, а объект был создан каким то классом
# А кто тогда создал MyClass

#
# MyClass = Метакласс()

print(MyClass.__class__)

# class B(MyClass):
#     a = 10
#     b = 20

B = type("B", (MyClass,), {"a": 10, "b": 20})

b = B()
print(b.a)
print(b.b)

# Вопрос 1
print(b.__class__)

# Вопрос 2
print(b.__class__.__class__)

# Вопрос 3
print(b.__class__.__class__.__class__)
print(b.__class__.__class__.__class__)
print(b.__class__.__class__.__class__.__class__)
