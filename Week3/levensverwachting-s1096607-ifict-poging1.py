

def levensverwachting(geslacht: str, roker: bool, sport: int,
                      alcohol: int, fastfood: bool)->float:
    """
    Calculates a life-expectancy over some simple inputs.
    :param geslacht: man / vrouw
    :param roker: smokes or not
    :param sport: exercise hours per week
    :param alcohol: units of alcohol per week
    :param fastfood: excessive fastfood consumption.
    :return: Life expectancy
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
