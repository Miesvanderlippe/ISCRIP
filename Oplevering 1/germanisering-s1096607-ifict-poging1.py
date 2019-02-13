from string import ascii_letters


def germaniseer(input_text: str) -> str:
    """
    'Germanise' a word. It converts a string in to one where every new word
    is upper cased.
    :param input_text: The text to be converted
    :return: The Converted Text
    """
    # Our new words will be stored here
    new_words = []

    # Break up sentence by spaces. Rough way to check separate words. Doesn't
    # really account for words after characters other than spaces.
    for word in input_text.split(' '):
        # We always have a first letter (make that upper case)
        new_word = word[0].upper()
        # The word isn't strictly longer than 1 char
        if len(word) > 1:
            # But if it is, append the rest of the word to the new word.
            new_word += word[1::]

        # Append the word to our new words list
        new_words.append(new_word)

    # Join the words again.
    return ' '.join(new_words)


def germaniseer_2(input_text: str) -> str:
    """
    'Germanise' a word. It converts a string in to one where every new word
    is upper cased.
    :param input_text: The text to be converted
    :return: The Converted Text
    """
    # First char is always uppercase. ( if it's not a letter, the next will
    # be uppercase anyways, no risk there)
    new_string = input_text[0].upper()

    # For each character after the first
    for i in range(1, len(input_text)):
        # If previous char is in the ascii letters range
        if input_text[i - 1] in ascii_letters:
            # Our current char is part of the same word (not uppercase)
            new_string += input_text[i]
        else:
            # Else, our current character is probably starting a new word
            new_string += input_text[i].upper()

    return new_string


if __name__ == '__main__':
    print(germaniseer('Geluk helpt soms, moed altijd.'))
    print(germaniseer(
        'Alleen hij is gelukkig die het geluk niet aan geluk te danken heeft.'
    ))

    print(germaniseer_2('Geluk helpt soms, moed altijd.'))
    print(germaniseer_2(
        'Alleen hij is gelukkig die het geluk niet aan geluk te danken heeft.'
    ))