
def dubbels(to_check:[]) -> []:
    """
    Checks for duplicate entries in array
    :param to_check: Array to check
    :return: Unique duplicates in array
    """
    # Words we've checked
    checked = []
    # Dupes found
    duplicates = []

    for entry in to_check:
        # Check if entry already seen, only add to dupes when not already duped
        if entry in checked and entry not in duplicates:
            duplicates.append(entry)
        # Always add to checked
        checked.append(entry)

    return duplicates


if __name__ == '__main__':
    print(dubbels([3, 9, 4, 3, 8, 7, 3, 4, 2]))
    print(dubbels([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(dubbels([8, 6, 9, 5, 7, 4, 8, 3]))
    print(dubbels(['0476-987394', '0498-837493', '0476-987394']))
