# https://dodona.ugent.be/nl/exercises/286850454/
from string import ascii_letters


def file_to_list(path: str) -> []:
    """
    Creates a list with every rule in a file. The linebreaks are trimmed off.
    :param path: path to file
    :return: list of rules
    """
    # Open file
    with open(path) as f:
        return [
            # For each rule (x) in the file (file.readlines) strip the \r \n etc
            x.strip() for x in f.readlines()
        ]


def omkeren(text: str):
    """
    Encode a string with 'Anna' encoding used in 1863 American civil war.
    :param text: Input
    :return: Encoded string
    """
    new = ""
    # The flipped _textual_ content of the string
    flipped = [x.lower() for x in reversed(text) if x in ascii_letters]

    # The positions of uppercase characters in the string
    uppercase_chars = [x for x, y in enumerate(text) if y.isupper()]

    # The special characters and their positions
    specials = {x:y for x, y in enumerate(text) if y not in ascii_letters}

    # The next letter to be encoded.
    # Kept separate because the position in the string is unrelated to the
    # letter encoded. (other chars keep their position)
    current = 0

    for index in range(0, len(text)):
        # If the current index is in an uppercase char in the source, it's a
        # letter and needs to be an uppercase letter in the encoded message.
        # All textual content will be reversed.
        if index in uppercase_chars:
            new += flipped[current].upper()
            current += 1
        # If the current char is a special char in the source, it needs not to
        # be a letter and remain at it's original position.
        elif index in specials.keys():
            new += specials[index]
        # If it's neither, it's a lowercase letter from the reversed textual
        # content.
        else:
            new += flipped[current]
            current += 1

    return new

def codec(text1: str, text2: str = None):
    result = "\n".join([omkeren(x) for x in file_to_list(text1)])

    if text2:
        with open(text2, "w") as f:
            f.write(result)
    else:
        print(result)

def gelijk(text1: str, text2: str):
    return "\n".join(file_to_list(text1)) == "\n".join(file_to_list(text2))


if __name__ == '__main__':
    print(omkeren('God bless our brave Confederates, Lord!'))
    print(omkeren('Dro lseta red efnoc Evarbruossel, Bdog!'))

    print(omkeren('Lee, Johnson, Smith, and Beauregard!'))
    print(omkeren('Help Jackson, Smith, and Johnson Joe,'))
    print(omkeren('To give them fits in Dixie, oh!'))

    codec('origineel.txt')
    codec('origineel.txt', 'gecodeerd.txt')
    codec('gecodeerd.txt')
    codec('gecodeerd.txt', 'gedecodeerd.txt')

    print(gelijk('origineel.txt', 'gecodeerd.txt'))
    print(gelijk('origineel.txt', 'gedecodeerd.txt'))
