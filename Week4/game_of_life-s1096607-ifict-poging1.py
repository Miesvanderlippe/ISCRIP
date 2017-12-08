

def aantalBuren(generatie: [[]], x: int, y: int) -> int:
    """
    Berekent het aantal nabijgelegen levende cellen.
    :param generatie: De huidige generatie
    :param x: x positie
    :param y: y positie
    :return: Aantal levende cellen in de buurt.
    """
    buren = 0
    # Alle posities om een punt.
    modifiers = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]

    for modifier in modifiers:
        pos_x = x + modifier[1]
        pos_y = y + modifier[0]

        # Controleerd of een positie binnen het veld valt
        if 0 <= pos_y < len(generatie) and \
                0 <= pos_x < len(generatie[0]):
            # Telt de levende cellen
            if generatie[pos_y][pos_x] == "X":
                buren += 1

    return buren


def toonGeneratie(generatie: [[]]) -> str:
    """
    Geeft het veld op een bepaalde manier weer.
    :param generatie: De generatie
    :return: Een printbare string.
    """
    return "\r\n".join([str(" ".join(row)) for row in generatie])


def volgendeGeneratie(generatie: [[]]) -> [[]]:
    """
    Berekent de volgende generatie
    :param generatie: De huidige generatie
    :return: De volgende generatie
    """

    # Een veld met dode cellen
    nieuwe_generatie = [
        [
            "O" for o in range(len(generatie[0]))
        ] for i in range(len(generatie))
    ]

    for y, row in enumerate(generatie):
        for x, cell in enumerate(row):
            buren = aantalBuren(generatie, x, y)

            # Alleen als een cel 2 of 3 buren heeft
            if cell == "X" and (buren == 2 or buren == 3):
                # Wordt een levende cel terug gezet op het bord
                nieuwe_generatie[y][x] = "X"

            # Of als er nog geen cel is en er 3 buren zijn
            if cell == "O" and buren == 3:
                # Wordt een levende cel terug gezet op het bord
                nieuwe_generatie[y][x] = "X"

    return nieuwe_generatie


def main() -> None:
    generatie = [["X", "O", "O", "O", "O", "O", "O", "O"] for x in range(0, 6)]

    for i in range(0, 4):
        print(toonGeneratie(generatie) + "\r\n")
        generatie = volgendeGeneratie(generatie)


if __name__ == '__main__':
    main()
