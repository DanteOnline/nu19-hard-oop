# -------------- Множественное наследование ------------------------

# Существует ситуация, когда невозможно выстроить цепочку классов-родителей.
# Неразрешимая ситуация множественного наследования в Python 3:

#            Mix        -- финальный класс-наследник 
#           /   \ 
#          Z     Q      -- первые классы-наследники
#          | \ / |  
#          | / \ |
#          X     Y      -- базовые классы

class X:
    def make_connection(self):
        print('x')


class Y:
    def make_connection(self):
        print('y')


class Z(X, Y):
    def make_connection(self):
        print('Z')


class Q(Y, X):
    def make_connection(self):
        print('Q')


class MixedClass(Z, Q):
    """ Смешанный класс
    """
    def make_connection(self):
        print('MIX-class')


mixed_conn = MixedClass()
#mixed_conn.make_connection()
print(MixedClass.__mro__)

# Traceback (most recent call last):
#  File "mro_intro01.py", line 72, in <module>
#    class MixedClass(Z, Q):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y
