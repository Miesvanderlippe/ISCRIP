import math

def is_palindrome(word: str) -> bool:
    # Word length
    word_length = len(word)
    # Half word length, floored. This ensures middle character isn't checked
    # if the word is of uneven length
    half_length = math.floor(word_length / 2)
    # First half of the word
    first_half = word[0:half_length]
    # Second half reversed
    second_half = ''.join(reversed(word[word_length - half_length::]))

    # If those match, it's a palindroom
    return first_half == second_half


if __name__ == '__main__':
    with open(input("File:\n")) as f:
        for line in f:
            stripped = line.strip().lower()
            if is_palindrome(stripped):
                print(stripped)
