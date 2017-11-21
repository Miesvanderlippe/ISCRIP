from string import ascii_lowercase, ascii_uppercase


def rot_shift(letter: str, shift: int) -> str:
    """
    Verschuift de letter n posities
    :param letter: letter
    :param shift: aantal posities
    :return: verleutelde letter
    """
    if letter in ascii_uppercase:
        return ascii_uppercase[((ascii_uppercase.index(letter) + shift) % 26)]
    elif letter in ascii_lowercase:
        return ascii_lowercase[((ascii_lowercase.index(letter) + shift) % 26)]
    else:
        return letter


def rotn_decode(input_str: str, shift: int) -> str:
    """
    Ontsleuteld een met rotn versleuteld bericht waarbij n (shift) het aantal
    posities is.
    :param input_str: versleuteld bericht
    :param shift: aantal verschoven posities
    :return: ontsleuteld bericht
    """
    return ''.join([rot_shift(x, shift * -1) for x in input_str])


def rotn_encode(input_str: str, shift: int) -> str:
    """
    Versleuteld een bericht met rotn waarbij n (shift) het aantal posities is.
    :param input_str: Bericht
    :param shift: Posities te verschuiven
    :return: Verleuteld bericht
    """
    return ''.join([rot_shift(x, shift * 1) for x in input_str])


def main()->None:
    mode = input("Encode(e) of decode (d)?\r\n").lower() == "e"
    message = input("Bericht:\r\n")
    shift = int(input("Shift:\r\n"))

    if mode:
        print(rotn_encode(message, shift))
    else:
        print(rotn_decode(message, shift))


if __name__ == '__main__':
    main()
