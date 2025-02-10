from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    min_x = 0
    max_x = len(data[0])
    min_y = 0
    max_y = len(data)

    data = sparse_grid(data, keepVal=True, true=ALPHA + UPPER + DIGITS)

    antennas = defaultdict(list)
    for x, y, v in data:
        antennas[v].append((x, y))

    antinodes = set()

    for antenna, points in antennas.items():
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                nx = p1[0]
                ny = p1[1]
                while True:
                    nx = nx + dx
                    ny = ny + dy
                    if min_x <= nx < max_x and min_y <= ny < max_y:
                        antinodes.add((nx, ny))
                    else:
                        break

    return len(antinodes)


if __name__ == "__main__":
    # LEGACY INPUT PARSING
    # ================================
    if (res := run(get_input())) is not None:
        print(res)
    # ================================

    # NEW INPUT PARSING
    # ================================
    # TODO
    # ================================
