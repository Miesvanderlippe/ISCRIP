

def levensverwachting(geslacht: str, roker: bool, sport: int,
                      alcohol: int, fastfood: bool)->float:
    """
    Berekent de levensverwachting van een persoon .
    :param geslacht: man / vrouw
    :param roker: rookt of niet
    :param sport: uren sport per week
    :param alcohol: eenheden alcohol per week
    :param fastfood: buitensporige fastfoodconsumptie
    :return: levensverwachting
    """
    basis_verwachting = 70

    if geslacht == "vrouw":
        basis_verwachting += 4

    if roker:
        basis_verwachting -= 5
    else:
        basis_verwachting += 5

    if sport == 0:
        basis_verwachting -= 3
    else:
        basis_verwachting += sport

    alcohol -= 7

    if alcohol > 0:
        basis_verwachting -= (alcohol * 0.5)

    if not fastfood:
        basis_verwachting += 3

    return basis_verwachting


def main()->None:
    print(levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10,
                            fastfood=True))

    print(levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5,
                            fastfood=True))

    print(levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0,
                            fastfood=False))

    print(levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14,
                            fastfood=True))

    print(levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4,
                            fastfood=False))


if __name__ == '__main__':
    main()
