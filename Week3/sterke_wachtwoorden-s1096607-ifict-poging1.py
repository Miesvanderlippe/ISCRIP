from string import punctuation


def password_strength(password: str)->int:
    """
    Controlleerd de sterkte van een wachtwoord aan de hand van een set
    arbitraire voorwaardes.
    :param password: Het wachtwoord om te controleren
    :return: score 0 - 5, zwak - sterk.
    """
    score = 0

    # Controle lengte
    if len(password) >= 8:
        score += 1

    # Als een van de karakters hetelfde is als hoofdletter
    # bevat het wachtwoord een hoofdletter
    if len([x for x in password if x == x.upper()]) > 0:
        score += 1

    # Als een van de karakters hetelfde is als kleine letter
    # bevat het wachtwoord kleine letter
    if len([x for x in password if x == x.lower()]) > 0:
        score += 1

    # Als een van de karakters een getal is
    # bevat het wachtwoord een cijfer
    if len([x for x in password if x.isdigit()]) > 0:
        score += 1

    # Als er een punt oid in zit
    if len([x for x in password if x in punctuation]) > 0:
        score += 1

    return score


def strength_to_word(strength: int)->str:
    """
    Zet de sterkte om in een woord.
    :param strength: Sterkte 0 - 5
    :return: zwak, matig, sterk
    """
    if strength < 3:
        return "zwak"

    if strength < 5:
        return "matig"

    return "sterk"


def main()->None:
    number = int(input("Aantal te testen wachtwoorden\r\n"))
    passwords = []

    for i in range(0, number):
        passwords.append(input("Wachtwoord{0}\r\n".format(i)))

    for password in passwords:
        print(strength_to_word(password_strength(password)))


if __name__ == '__main__':
    main()
