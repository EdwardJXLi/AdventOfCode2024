from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    grid, X, Y = char_grid(data)
    count = 0

    for x in range(1, X - 1):
        for y in range(1, Y - 1):
            w1 = grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]
            w2 = grid[y-1][x+1] + grid[y][x] + grid[y+1][x-1]
            if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM"):
                count += 1

    return count


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
