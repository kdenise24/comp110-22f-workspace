"""EX07 - Dictionary Functions."""
__author__ = "730566062"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of strings, it should return a dictionary that inverts the keys and values."""
    inverted: dict[str, str] = {}
    for key in original:
        if original[key] in inverted:
            raise KeyError
        inverted[original[key]] = key
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    """Given a dictionary of names an colors, it returns the color that apppears the most."""
    i: int = 0
    output: str = ""
    number_ofcolors: dict[str, int] = {}
    for color in input:
        if input[color] in number_ofcolors:
            number_ofcolors[input[color]] = number_ofcolors[input[color]] + 1
        else:
            number_ofcolors[input[color]] = 1
    for color in number_ofcolors:
        if number_ofcolors[color] > i:
            i = number_ofcolors[color]
            output = color
    return output


def count(input: list[str]) -> dict[str, int]:
    """Given a list of values it should return a dictionary with the counts of each value in the input list."""
    dict_ofcounts: dict[str, int] = {}
    for item in range(0, len(input)):
        if input[item] in dict_ofcounts:
            dict_ofcounts[input[item]] = dict_ofcounts[input[item]] + 1
        else:
            dict_ofcounts[input[item]] = 1
    return dict_ofcounts