# Множественное наследование

# В классах "нового стиля" (в Python 3 все классы - нового стиля) реализуется
# алгоритм C3-линеаризации для выстраивания "цепочки" классов-родителей:
# https://en.wikipedia.org/wiki/C3_linearization

class A:
    def mix(self):
        print('Class A')


class B(A):
    pass
    # def mix(self):
    #     print('Class B')


class C:
    pass
    # def mix(self):
    #     print('Class C')


class D(C):
    def mix(self):
        print('Class D')


class E(B, D):
    def mix(self):
        print('Class E')


class BC(B, C):
    def mix(self):
        print('Class BC')


class My(C, B):
    pass

    # def mix(self):
    #     print('Class My')


# Чтобы узнать порядок разрешения методов, который в данном случае принял Python,
# можно посмотреть значение атрибута __mro__ класса:
# BC, B, C, A
# print(BC.__mro__)
# print(E.__mro__)
print(My.__mro__)

# Комментируя в разном порядке в каждом классе метод mix
# можно посмотреть, как меняется поведение класса My:

e = My()
e.mix()
