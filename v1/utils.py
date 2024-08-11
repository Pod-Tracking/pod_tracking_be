from .enums.color_enum import MtgColor

def process_colors(color_list: list) -> str:
    color_values = []
    for color in color_list:
        if color in MtgColor.__members__:
            color_values.append(MtgColor[color].value)
    return ', '.join(color_values)
