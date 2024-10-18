from enum import Enum

class DeckType(Enum):
    COMMANDER = 'commander'
    STANDARD = 'standard'
    MODERN = 'modern'
    PIONEER = 'pioneer'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

