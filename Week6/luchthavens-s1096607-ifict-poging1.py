from math import radians, atan2, sqrt, cos, sin
from typing import Union, Optional, Any
from os import path


def lees_luchthavens(bestandsnaam: str) -> dict:
    """
    Haalt de luchtavens op uit het bestand
    :param bestandsnaam: de naam van het bestand met luchthavens
    :return: de luchthavens
    """
    airports = dict()

    with open(path.dirname(__file__) + '/' + bestandsnaam) as f:
        inhoud = f.readlines()

        for row in inhoud[1:]:
            row = row.split('\t')
            airports.update({row[0][1:-1]: (
                float(row[1]), float(row[2]), row[3], row[4])})

    return airports


def afstand(code_1: str, code_2: str, luchthavens: dict) -> float:
    """
    De afstand tussen twee luchthavens
    :param code_1: luchthaven 1
    :param code_2: luchthaven 2
    :param luchthavens: de lijst met luchthavens
    :return: de afstand tussen de twee vliegvelden
    """
    lat_1, long_1 = luchthavens[code_1][0:2]
    lat_2, long_2 = luchthavens[code_2][0:2]

    return 6372.795 * atan2(
        sqrt(pow(cos(radians(lat_2)) * sin(radians(long_1) - radians(long_2)),
                 2) +
             pow(cos(radians(lat_1)) * sin(radians(lat_2)) -
                 sin(radians(lat_1)) * cos(radians(lat_2)) *
                 cos(radians(long_1) - radians(long_2)), 2)),
        sin(radians(lat_1)) * sin(radians(lat_2)) +
        cos(radians(lat_1)) * cos(radians(lat_2)) *
        cos(radians(long_1) - radians(long_2)))


def tussenlanding(code_1: str, code_2: str, luchthavens: dict,
                  reikwijdte: int = 4000) -> Union[Optional[str], Any]:
    """
    Probeert een tussenlanding te maken tussen twee vliegvelden die anders te
    ver uit elkaar liggen.
    :param code_1: Start vliegveld
    :param code_2: Eind vliegveld
    :param luchthavens: Lijst met luchthavens
    :param reikwijdte: Bereik van het vliegtuig
    :return: Code van eventueel tussenvliegveld
    """
    distance = afstand(code_1, code_2, luchthavens)
    smallest = distance * 10000
    code = None

    for airport in luchthavens:
        if airport not in [code_1, code_2]:
            first = afstand(code_1, airport, luchthavens)
            second = afstand(airport, code_2, luchthavens)
            thirth = first + second

            if first <= reikwijdte and second <= reikwijdte:
                if thirth < smallest:
                    smallest = thirth
                    code = airport

    if code is None or distance < reikwijdte:
        return None
    else:
        return code


def main() -> None:
    luchthavens = lees_luchthavens('luchthavens.txt')

    print(luchthavens)
    print(luchthavens['ADK'])
    print(luchthavens['DCA'])
    print(luchthavens['4OM'])
    print('{distance:.8f}'.format(distance=afstand('P60', 'MSN', luchthavens)))
    print('{distance:.8f}'.format(distance=afstand('ADK', 'DCA', luchthavens)))
    print(tussenlanding('ADK', 'DCA', luchthavens, 4000))


if __name__ == '__main__':
    main()
