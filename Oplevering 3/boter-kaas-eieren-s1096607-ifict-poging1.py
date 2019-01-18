
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


def leesBord(input_file: str) -> []:
    """
    Reads board into array
    :param input_file: file location
    :return: list of lines in board
    """
    return file_to_list(input_file)


def toonBord(bord: []) -> str:
    """
    Creates a printable string of a board
    :param bord: board
    :return: printable board
    """
    # Separate all rows by newline
    return '\n'.join(
        # Displayed board has spaces in between chars
        ' '.join(
            # Displayed board has dots instead of blanks
            [x for x in regel.replace(' ', '.')]
        )
        for regel in bord
    )


def get_column(array: [[]], index: int) -> []:
    """
    Gets a column out of a multi dimensional list
    :param array: array
    :param index: column to get (0-based)
    :return: the column
    """
    return [
        # Return the index of each row
        row[index] for row in array
    ]


def winnaar(bord: []) -> str:
    # By default, no-one wins
    x_wins = False
    o_wins = False

    # All possible winlines on the board
    winlines = [
        # Horizontal lines
        bord[0], bord[1], bord[2],
        # Vertical lines
        get_column(bord, 0),
        get_column(bord, 1),
        get_column(bord, 2),
        # Diagonal lines
        bord[0][0] + bord[1][1] + bord[2][2],
        bord[2][0] + bord[1][1] + bord[0][2],
    ]

    # Check each winline
    for winline in winlines:
        # A set contains every unique char in a string
        # Join the set back into a string
        winner = ''.join(set(winline))

        # If it's just an X, X wins
        if winner == 'X':
            x_wins = True
        # If it's just an O, O wins
        elif winner == 'O':
            o_wins = True
        # If it's a space, or a mix of multiple chars
        # No-one wins

    # If no-one wins, or both win
    if x_wins == o_wins:
        # It's a draw
        return ''
    elif x_wins:
        return 'X'
    elif o_wins:
        return 'O'



if __name__ == '__main__':
    print(leesBord('tictactoe1.txt'))
    print(leesBord('tictactoe2.txt'))
    print(leesBord('tictactoe3.txt'))

    print(toonBord(['XXO', 'OOX', 'XOX']))

    results = [
        winnaar(['OX ', 'OX ', ' X ']),
        winnaar(['OOO', ' XX', 'X  ']),
        winnaar(['XXO', 'OOX', 'XOX'])
    ]

    for result in results:
        if result == '':
            print('gelijkspel')
        else:
            print('{0} wint'.format(result))