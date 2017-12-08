import copy
POSSIBLE_ORIENTATIONS = ['^', '>', 'v', '<']
ANTS = ['🢁', '🢂', '🢃', '🢀']


def clamp(cur: int, minimum: int, maximum: int) -> int:
    """
    Limiteert een waarde tussen een minumum en maximum.
    :param cur: Huidige waarde
    :param minimum: Minimum waarde
    :param maximum: Maximum waarde
    :return: Minumum wanneer cur < minumum, maxiumum wanneer cur > maximum
    anders cur.
    """
    return max(minimum, min(cur, maximum))


def orientation(direction: str) -> int:
    """
    Geeft de richting van een pijl. 0 is omhoog, 1 is rechts, 2 onder, 3 links
    :param direction: de pijl
    :return: De richting
    """
    return POSSIBLE_ORIENTATIONS.index(direction)


def rotate(direction: str, step: int = 1) -> str:
    """
    Draait de pijl een n stappen naar rechts. Negatief is dus linksaf draaien.
    :param direction: de huidige pijl
    :param step: het aantal kwarten om te draaien
    :return: de nieuwe pijl
    """
    return POSSIBLE_ORIENTATIONS[(orientation(direction) + step) % 4]


def rooster(rows: int, orientations: str) -> [[]]:
    """
    Maakt een raster aan aan de hand van een gegeven lijst orientaties en een
    breedte van de rijen.
    :param rows: breedte van de rijen
    :param orientations: een reeks pijlen
    :return: het grid
    """
    return [
        list(orientations[i:i+rows]) for i in range(0, len(orientations), rows)
    ]


def tekst_pos(grid: [[]], pos: (int, int)) -> str:
    """
    Geeft een grid met daarin aangegeven wat de huidige positie is.
    :param grid: Het grid.
    :param pos: De positie om te highlighten
    :return: Een printbare string met hierin aangegeven de positie
    """
    new_grid = copy.deepcopy(grid)
    new_grid[pos[0]][pos[1]] = ANTS[orientation(new_grid[pos[0]][pos[1]])]
    return tekst(new_grid)


def tekst(grid: [[]]) -> []:
    """
    Een printbaar grid.
    :param grid: Het grid.
    :return: Een printbaar grid.
    """
    return "\r\n".join([" ".join(row) for row in grid])


def stap(grid: [[]], pos: (int, int)) -> ([[]], (int, int)):
    """
    Simuleert een stap van de mier.
    :param grid: Het huidige grid.
    :param pos: De huidige positie (x, y).
    :return: Een nieuw grid en een nieuwe positie.
    """
    x = pos[0]
    y = pos[1]

    direction = orientation(grid[x][y])
    # Wat er moet gebeuren met de coordinaten voor de volgende stap.
    modifiers = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # Nieuwe x en y uitrekenen. Mogen niet buiten het velkd vallen.
    new_x = clamp(x + modifiers[direction][0], 0, len(grid[0]) - 1)
    new_y = clamp(y + modifiers[direction][1], 0, len(grid) - 1)

    # Pijltje op de oude positie draaien.
    grid[x][y] = rotate(grid[x][y])

    return grid, (new_x, new_y)


def stappen(grid: [[]]) -> ([[]], [(int, int)], []):
    """
    Simuleert het pad dat de mier zal lopen.
    :param grid:
    :return:
    """
    x = len(grid) - 1
    y = 0
    tar_y = len(grid[0]) - 1
    tar_x = 0
    steps = [(x, y)]

    while x != tar_x or y != tar_y:
        print(tekst_pos(grid, (x, y)) + "\r\n-------")
        grid, (x, y) = stap(grid, (x, y))
        steps.append((x, y))

    print(tekst_pos(grid, (x, y)))
    return grid, (x, y), steps


def main() -> None:
    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    vierkant, pos, steps = stappen(vierkant)

    print(steps)


if __name__ == '__main__':
    main()
