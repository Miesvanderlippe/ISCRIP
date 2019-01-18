
def schrikkeljaar(year: int) -> bool:
    """
    Checks if a year is a 'schrikkeljaar' (day with 366 days)
    :param year: year to check
    :return: whether it's a schrikkeljaar
    """
    # Every 4th century has years with 366 days.
    # Every 4th year in those centuries have 366 days
    return (year % 400 < 100) and (year % 4 == 0)


if __name__ == '__main__':
    if schrikkeljaar(int(input("Jaartal:\n"))):
        print("schrikkeljaar")
    else:
        print("geen schrikkeljaar")