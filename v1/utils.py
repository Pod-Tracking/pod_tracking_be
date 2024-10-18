from .enums.color_enum import MtgColor
from .enums.deck_type_enum import DeckType
from .enums.tcg_type_enum import TcgType


def process_colors(color_list: list) -> str:
    color_values = []
    for color in color_list:
        if color in MtgColor.__members__:
            color_values.append(MtgColor[color].value)
        else:
            raise ValueError(f"Invalid color value: {color}")
    return ', '.join(color_values)

def validate_tcg_type(tcg_type: str) -> str:
    if tcg_type in TcgType.__members__:
        return tcg_type
    else:
        raise ValueError(f"Invalid TCG type: {tcg_type}")

def validate_deck_type(deck_type: str) -> str:
    if deck_type in DeckType.__members__:
        return deck_type
    else:
        raise ValueError(f"Invalid Deck type: {deck_type}")
