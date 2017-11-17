from string import ascii_lowercase, ascii_uppercase


def rot_shift(letter: str, shift: int) -> str:
    if letter in ascii_uppercase:
        return ascii_uppercase[((ascii_uppercase.index(letter) + shift) % 26)]
    elif letter in ascii_lowercase:
        return ascii_lowercase[((ascii_lowercase.index(letter) + shift) % 26)]
    else:
        return letter


def rotn_decode(input_str: str, shift: int) -> str:
    return ''.join([rot_shift(x, shift * -1) for x in input_str])


def rotn_encode(input_str: str, shift: int) -> str:
    return ''.join([rot_shift(x, shift * 1) for x in input_str])


def main()->None:
    print(rotn_decode("Ylluly boguhog ymn", 20))
    print(rotn_decode(rotn_encode("Dit is een geheim", 20), 20))


if __name__ == '__main__':
    main()
