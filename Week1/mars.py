import math


def readable_time(inp: float)->str:
    """
    Formats seconds to days, hours, minutes & seconds
    :param inp: timespan in seconds
    :return: string {0}d {1}h {2}m {3}s
    """
    sec = round(inp)

    days = math.floor(sec / 86400)
    sec -= 86400 * days

    hrs = math.floor(sec / 3600)
    sec -= 3600 * hrs

    mins = math.floor(sec / 60)
    sec -= 60 * mins

    return "{0}d {1}h {2}m {3}s".format(days, hrs, mins, sec)


def main()->None:
    sol_days = int(input("sol \r\n"))
    earth_sec = sol_days * 35.244 + (sol_days * 60 * 39) + \
        (sol_days * 60 * 60 * 24)

    print(readable_time(earth_sec))


if __name__ == '__main__':
    main()
