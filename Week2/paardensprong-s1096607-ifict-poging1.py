import string


def coordinates(inp: str)->tuple:
    """
    Extracts coordinates from positions in Chess
    :param inp: Coordinates (D4)
    :return: X & Y Coordinates
    """
    x = int(inp[1])
    y = int(string.ascii_lowercase.index(inp[0])) + 1

    return x, y


def is_valid_move(set1: tuple, set2: tuple)->bool:
    """
    Checks move of horse in chess for validity.
    :param set1: Starting position
    :param set2: Ending position
    :return: Whether or not the move is valid
    """
    # Twee stappen de ene kant op, en een stap de andere kant op is een geldige
    # paarden sprong.
    return (abs(set1[0] - set2[0]) == 2 and abs(set1[1] - set2[1]) == 1) or \
        (abs(set1[0] - set2[0]) == 1 and abs(set1[1] - set2[1]) == 2)


def main()->None:
    pos1 = input("Pos 1\r\n")
    pos2 = input("Pos 2\r\n")
    set1 = coordinates(pos1)
    set2 = coordinates(pos2)

    print("het paard kan {0}springen van {1} naar {2}".format(
        ["niet ", ""][is_valid_move(set1, set2)], pos1, pos2))


if __name__ == '__main__':
    main()
