import copy
POSSIBLE_ORIENTATIONS = ['^', '>', 'v', '<']


def clamp(cur: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(cur, maximum))


def orientation(direction: str) -> int:
    return POSSIBLE_ORIENTATIONS.index(direction)


def rotate(direction: str, step: int = 1) -> str:
    return POSSIBLE_ORIENTATIONS[(orientation(direction) + step) % 4]


def rooster(rows: int, orientations: str) -> [[]]:
    return [
        list(orientations[i:i+rows]) for i in range(0, len(orientations), rows)
    ]


def tekst_pos(grid: [[]], pos: (int, int)) -> str:
    grid[pos[0]][pos[1]] = "[" + grid[pos[0]][pos[1]] + "]"
    return tekst(grid).replace(" [", "[").replace("] ", "]")


def tekst(grid: [[]]) -> []:
    return "\r\n".join([" ".join(row) for row in grid])


def stap(grid: [[]], pos: (int, int)) -> ([[]], (int, int)):

    x = pos[0]
    y = pos[1]

    direction = orientation(grid[x][y])
    modifiers = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    new_x = clamp(x + modifiers[direction][0], 0, len(grid[0]) - 1)
    new_y = clamp(y + modifiers[direction][1], 0, len(grid) - 1)

    grid[x][y] = rotate(grid[x][y])

    return grid, (new_x, new_y)


def stappen(grid: [[]]) -> ([[]], [(int, int)]):
    x = len(grid) - 1
    y = 0
    tar_y = len(grid[0]) - 1
    tar_x = 0
    steps = [(x, y)]

    while x != tar_x or y != tar_y:
        print(tekst_pos(copy.deepcopy(grid), (x, y)))
        grid, (x, y) = stap(grid, (x, y))
        steps.append((x, y))

    print(steps)
    print(tekst_pos(copy.deepcopy(grid), (x, y)))
    return grid, (x, y)


def main() -> None:
    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    stappen(vierkant)


if __name__ == '__main__':
    main()
