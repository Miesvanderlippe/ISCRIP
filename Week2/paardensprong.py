import string


def coordinates(inp: str)->tuple:
    """
    Extracts coordinates from positions in Chess
    :param inp: Coordinates (D4)
    :return: X & Y Coordinates
    """
    x = int(inp[1])
    y = int(string.ascii_lowercase.index(inp[0]))

    return x, y


def main()->None:
    pos1 = input("Pos 1")
    pos2 = input("Pos 2")
    set1 = coordinates(pos1)
    set2 = coordinates(pos2)

    valid = (abs(set1[0] - set2[0]) == 2 and abs(set1[1] - set2[1]) == 1) or \
        (abs(set1[0] - set2[0]) == 1 and abs(set1[1] - set2[1]) == 2)

    print("het paard kan {0}springen van {1} naar {2}".format(
        ["niet ", ""][valid], pos1, pos2))


if __name__ == '__main__':
    main()
