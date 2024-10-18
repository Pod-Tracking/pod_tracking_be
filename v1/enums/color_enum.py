from enum import Enum

class MtgColor(Enum):
    W = 'White'
    U = 'Blue'
    B = 'Black'
    R = 'Red'
    G = 'Green'
    C = 'Colorless'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class OnePieceColor(Enum):
    Y = 'Yellow'
    R = 'Red'
    G = 'Green'
    U = 'Blue'
    P = 'Purple'
    B = 'Black'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    