from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    tpm, X, Y = int_grid(data)

    def travel(x, y):
        if tpm[y][x] == 9:
            return 1
        
        r = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < X and 0 <= y + dy < Y and tpm[y + dy][x + dx] == tpm[y][x]+1:
                r += travel(x + dx, y + dy)

        return r
            
    tot = 0
    for y in range(Y):
        for x in range(X):
            if tpm[y][x] == 0:
                tot += travel(x, y)

    return tot


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
