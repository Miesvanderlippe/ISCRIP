from string import ascii_lowercase

vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set(ascii_lowercase).difference(vowels)


def medeklinkers(filename: str) -> {}:
    """
    Haalt te medeklinkers en hun vertalingen op uit het vertaal bestand
    :param filename: (relatief) pad naar het vertaalbestand
    :return: Een dictionary met de letters (key) en hun doubledutch vertaling
    """
    with open(filename) as file:
        dict = {
            line[0]: line[1]
            for line in [
                x.strip().replace(' ', '').split('-') for x in file.readlines()
            ]
        }

    # Only consonants should be translated
    assert(not any([x for x in dict.keys() if x not in consonants]))
    # All consonants are translated
    assert(len(dict.keys()) == len(consonants))
    # All translations start with their respective char
    assert(all([key == dict[key][0] for key in dict]))

    return dict


def vertaalWoord(word: str, dictionary: {}) -> str:
    """
    Vertaald een enkel woord naar DoubleDutch
    :param word: Het woord om te vertalen
    :param dictionary: De vertaal-dictionary om te gebruiken
    :return: Het vertaalde woord
    """
    encoded = ""
    index = 0

    while index < len(word):
        cur_char = word[index]
        # +1 for 0 indexed array, +1 to check if next is available
        if index + 2 > len(word):
            next_char = ""
        else:
            next_char = word[index + 1]
        # 2 identical chars are encoded in a special way
        if cur_char.lower() == next_char.lower():
            if cur_char.lower() in vowels:
                encoded += "squat" + cur_char + "h"
            else:
                encoded += "squa" + cur_char
            # Skip upcoming char, we handled that
            index += 1
        # If an encoding is available for a char use it
        elif cur_char.lower() in dictionary.keys():
            if cur_char.isupper():
                encoded += (dictionary[cur_char.lower()]).capitalize()
            else:
                encoded += dictionary[cur_char.lower()]
        # Otherwise use the char itself (vowels etc)
        else:
            encoded += cur_char

        index += 1

    return encoded


def vertaal(sentence: str, dictionary: {}) -> str:
    """
    Vertaald een hele zin woord voor woord naar DoubleDutch
    :param sentence: De zin om te vertalen
    :param dictionary: De vertaal-dictionary om te gebruiken
    :return: De vertaalde zin
    """
    return ' '.join([
        vertaalWoord(word, dictionary) for word in sentence.split(' ')
    ])


def main() -> None:
    dutchLetter = medeklinkers('dutchLetters.txt')

    print(dutchLetter['s'])
    print(dutchLetter['q'])
    print(dutchLetter['d'])
    # print(dutchLetter['e'])

    print(vertaalWoord('took', dutchLetter))
    print(vertaalWoord('BAMBOO', dutchLetter))
    print(vertaalWoord('Yesterday', dutchLetter))

    print(vertaal('I took a walk to the park yesterday.', dutchLetter))


if __name__ == '__main__':
    main()