
def pad_str(string: str, padding: int) -> str:
    """
    Voegt spaties toe aan een string tot het totaal een bepaalde breedte heeft
    :param string: De string
    :param padding: Hoe breed deze minimaal moet zijn
    :return: De gepadde string zoals: "      str"
    """
    return " " * (padding - len(string)) + string


def printbaar_vierkant(vierkant: [[]]) -> str:
    """
    Geeft het vierkant terug in een makkelijk te printen vorm
    :param vierkant: Het vierkant
    :return: Een te printen string
    """
    return "\r\n".join(
        ["".join(
            [pad_str(str(cijfer), 8) for cijfer in lijst]
        ) for lijst in vierkant]
    )


def vierkant(formaat: int, basis: int = 1) -> [[]]:
    """
    Genereert een vierkant van pascal aan de hand van de gegeven parameters.
    :param formaat: Het formaat van het vierkant
    :param basis: Het getal op de zijlijnen
    :return: Een list list met de getallen in het vierkant.
    """
    # De bovenste rij is gewoon het basis getal
    rows = [[basis for _ in range(0, formaat)]]

    # Voor elke rij
    for row in range(0, formaat - 1):
        # Het eerste getal van elke rij is het basisgetal
        new_row = [basis]
        # Het vorige getal wordt dan dus even hierop gezet
        prev_num = basis
        # De vorige rij kan opgehaald worden uit de rijen die we al hebben
        prev_row = rows[-1]
        for pos in range(0, formaat - 1):
            # We voegen een nieuw getal toe aan de regel die we opbouwen
            new_row.append(prev_row[pos + 1] + prev_num)
            # En stellen het nieuwe vorige nummer in
            prev_num = new_row[-1]

        # We voegen de rij toe aan de bestaande rijen
        rows.append(new_row)

    return rows


def main() -> None:
    formaat = int(input("Hoe groot wilt u het vierkant?\r\n"))
    basis = int(input("Wel getal wilt u als basis getal gebruiken?\r\n"))
    print(printbaar_vierkant(vierkant(formaat, basis)))


if __name__ == '__main__':
    main()

