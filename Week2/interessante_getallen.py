

def totaal_cijfers(getal: int) -> int:
    """
    De som van de cijfers in een getal
    :param getal: Het getal
    :return: De som
    """
    return sum([int(x) for x in str(getal)])


def int_getal(test: int) -> int:
    """
    Geeft het eerste getal waarvan de cijfers het getal vormen dat ook deelbaar
    is door het getal.
    :param test: Het getal
    :return: Het deelbare, optelbare getal
    """
    num = test

    while not (totaal_cijfers(num) == test):
        num += test

    return num


def main()->None:
    inputs = []
    aantal_inputs = int(input("Getal tussen 0 en 50:\r\n"))

    for i in range(0, aantal_inputs):
        inputs.append(int(input("Getal tussen 0 en 100:\r\n")))

    for i in inputs:
        print(int_getal(i))


if __name__ == '__main__':
    main()
