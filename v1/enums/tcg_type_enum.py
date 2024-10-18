from enum import Enum


class TcgType(Enum):
    MAGIC = 'magic_the_gathering'
    ONE_PIECE = 'one_piece'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
