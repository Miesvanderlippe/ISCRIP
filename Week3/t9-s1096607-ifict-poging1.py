

def letter_to_t9(char: str)->int:
    """
    The dirtiest of functions to translate a letter to a number on a phonepad.
    :param char: Uppercase letter
    :return: Number on keypad
    """
    if char in "ABC":
        return 2
    if char in "DEF":
        return 3
    if char in "GHI":
        return 4
    if char in "JKL":
        return 5
    if char in "MNO":
        return 6
    if char in "PQRS":
        return 7
    if char in "TUV":
        return 8
    if char in "WXYZ":
        return 9
    return 0


def T9(input_str: str)->str:
    """
    Translates a string into positions on a phone's keypad.
    :param input_str: Input string ( case insensitive)
    :return: positions on keypad
    """
    input_str = input_str.upper()

    return ''.join([str(letter_to_t9(x)) for x in input_str])


def main()->None:
    print(T9(input("Voer uw tekst in:\r\n")))


if __name__ == '__main__':
    main()
