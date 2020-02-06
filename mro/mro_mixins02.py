# -------------- Множественное наследование ------------------------

print('--------------- Сложности множественного наследования ----------------')

import random


# Классы примеси, mixin

class MusicGenre:
    ''' Базовый класс жанра для музыкальной библиотеки.
        Определяет название жанра и его рейтинг в библиотеке.
    '''
    pass


class DrumAndBass(MusicGenre):
    pass


group = DrumAndBass()


class PromoConcert:
    ''' Промо-концерт улучшает рейтинг исполнителя
    '''
    pass


class Gossip:
    ''' Сплетни, слухи снижают рейтинг
    '''
    pass


# Класс, использующий механизм множественного наследования
class SuperDrums(DrumAndBass, PromoConcert, Gossip):
    pass


# Узнаем, порядок разрешения методов
print(SuperDrums.__mro__)


class Figure:

    def draw(self):
        pass


class PlottableMixin:

    def plot(self):
        pass


class Rect(Figure, PlottableMixin):
    pass


class SpecialLine(Figure):
    pass
