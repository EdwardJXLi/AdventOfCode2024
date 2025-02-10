from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    N_KEYPAD = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"]
    ]

    D_KEYPAD = [
        [None, "^", "A"],
        ["<", "v", ">"]
    ]

    N_MAPKEY = {}
    D_MAPKEY = {}

    for y, row in enumerate(N_KEYPAD):
        for x, key in enumerate(row):
            if key is not None:
                N_MAPKEY[key] = (x, y)
    
    for y, row in enumerate(D_KEYPAD):
        for x, key in enumerate(row):
            if key is not None:
                D_MAPKEY[key] = (x, y)

    @cache
    def generate_paths(numpad, start, end):
        keypad = N_KEYPAD if numpad else D_KEYPAD
        queue = [(start, "")]
        paths = []

        while queue:
            pos, path = queue.pop(0)
            x, y = pos

            if (x, y) == end:
                paths.append(path + "A")
                continue

            min_x, max_x, min_y, max_y = min_max_xy([pos, end])

            for dx, dy, ins in [(0, 1, "v"), (1, 0, ">"), (0, -1, "^"), (-1, 0, "<")]:
                nx, ny = x + dx, y + dy
                if min_x <= nx <= max_x and min_y <= ny <= max_y and keypad[ny][nx]:
                    queue.append(((nx, ny), path + ins))

        return paths
    
    @cache
    def solve(limit, moves, depth=0):
        keypad = N_KEYPAD if depth == 0 else D_KEYPAD
        mapkey = N_MAPKEY if depth == 0 else D_MAPKEY
        cur = "A"

        total = 0
        for move in moves:
            paths = generate_paths(keypad is N_KEYPAD, mapkey[cur], mapkey[move])
            cur = move

            if depth == limit:
                total += min(map(len, paths))
            else:
                total += min(solve(limit, path, depth=depth+1) for path in paths)
        return total

    
    tot = 0
    for line in data:
        # complexity = solve(2, line) * int(line[:-1])
        complexity = solve(25, line) * int(line[:-1])
        tot += complexity
    
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
