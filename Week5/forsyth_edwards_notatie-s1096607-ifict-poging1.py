

def replacer(char: str, sep: str = '*') -> str:
    """
    Functie om cijfers te vervangen met N maal de seperator
    :param char: De invoer
    :param sep: De separator
    :return: N maal de seperator of de letter
    """
    if char.isdigit():
        return sep * int(char)
    return char


def fen2grid(string: str, separator: str = '*') -> []:
    """
    Zet een Fen notatie om in een grid
    :param string: De Fen notatie
    :param separator: De separator
    :return: De grid in een lijst met regels
    """
    secties = string.split('/')
    return [
        "".join(
            [replacer(char, separator) for char in sectie]
        )
        for sectie in secties
    ]


def grid2fen(string: str, separator: str = '*') -> str:
    """
    Zet een volledig uitgeschreven grid om in een Fen notatie
    :param string: De grid
    :param separator: De gebruikte separator
    :return: De fen notatie
    """
    # Breekt de grid op in secies van 8 regels
    lines = [
        str(string[i:i + 8]) for i in
        range(0, len(string), 8)
    ]
    result = []

    for line in lines:
        for i in range(8, 0, -1):
            # Slordig en goor, maar het werkt!
            line = line.replace(separator * i, str(i))

        result.append(line)

    return "/".join(result)


def main() -> None:

    if input("Kies een van de opties:\r\n1) Fen omzetten naar grid\r\n" +\
             "2) Grid omzetten naar Fen notatie\r\n") == "1":

        user_input = input("Geef uw Fen\r\n")
        separator = input("Geef uw seperator\r\n")

        if len(separator) != 1:
            print("\r\n".join(fen2grid(user_input)))
        else:
            print("\r\n".join(fen2grid(user_input, separator)))

    else:

        user_input = input("Geef uw Grid (zonder enters)\r\n").replace("/", "")
        separator = input("Geef uw seperator\r\n")

        if len(separator) != 1:
            print(grid2fen(user_input))
        else:
            print(grid2fen(user_input, separator))


if __name__ == '__main__':
    main()
