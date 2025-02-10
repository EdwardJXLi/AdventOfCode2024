from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    grid, X, Y = single_char_grid(data)

    visited = [[False] * X for _ in range(Y)]

    def check_same(x, y, c):
        if 0 <= x < X and 0 <= y < Y:
            return grid[y][x] == c
        return False

    def get_data(x, y):
        area = 0
        edges = 0
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            area += 1

            c = grid[y][x]
            if not check_same(x+1, y, c) and not check_same(x, y+1, c):
                edges += 1
            if not check_same(x-1, y, c) and not check_same(x, y-1, c):
                edges += 1
            if not check_same(x-1, y, c) and not check_same(x, y+1, c):
                edges += 1
            if not check_same(x+1, y, c) and not check_same(x, y-1, c):
                edges += 1
            if check_same(x+1, y, c) and check_same(x, y+1, c) and not check_same(x+1, y+1, c):
                edges += 1
            if check_same(x-1, y, c) and check_same(x, y-1, c) and not check_same(x-1, y-1, c):
                edges += 1
            if check_same(x-1, y, c) and check_same(x, y+1, c) and not check_same(x-1, y+1, c):
                edges += 1
            if check_same(x+1, y, c) and check_same(x, y-1, c) and not check_same(x+1, y-1, c):
                edges += 1

            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y and grid[ny][nx] == grid[y][x]:
                    stack.append((nx, ny))
        # detect numnber of sides
        # for x, y in [(x, y), (x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        #     if 0 <= x < X and 0 <= y < Y and grid[y][x] != grid[y][x]:
        #         sides += 1

        return area, edges

    price = 0
    for y in range(Y):
        for x in range(X):
            if not visited[y][x]:
                area, perimeter = get_data(x, y)
                price += area * perimeter
    
    return price


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
