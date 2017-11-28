

def letter_to_t9(char: str)->int:
    """
    Vertaald een letter naar een positie op het T9 toetsenbord
    :param char: Letter (hoofdletter)
    :return: Cijfer op het toetsenbord
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
    Vertaald een woord naar de T9 string
    :param input_str: Input string ( hoofdletter ongevoelig)
    :return: Posities op het toetsenbord
    """
    input_str = input_str.upper()

    return ''.join([str(letter_to_t9(x)) for x in input_str])


def main()->None:
    print(T9(input("Voer uw tekst in:\r\n")))


if __name__ == '__main__':
    main()
