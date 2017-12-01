

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


def GSMoniemen(woord1: str, woord2: str)->bool:
    """
    Controleeerd of 2 woorden met dezelfde cijfers op een T9 toetsenbord
    geschreven kunnen worden
    :param woord1: Woord 1
    :param woord2: Woord 2
    :return: of ze met dezelfde toeten geschreven worden.
    """
    return T9(woord1) == T9(woord2)


def main()->None:
    woord1 = input("Woord 1:\r\n")
    woord2 = input("Woord 2:\r\n")

    print(GSMoniemen(woord1, woord2))


if __name__ == '__main__':
    main()
