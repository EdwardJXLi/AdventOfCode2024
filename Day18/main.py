from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    # Demo data
    # X = Y = 6 + 1

    # Input data
    X = Y = 70 + 1

    map = []
    for line in data:
        x, y = ints(line)
        map.append((x, y))

    def travel(n):
        # print(n)
        start = (0, 0)
        end = (X - 1, Y - 1)
        block = set(map[:n])

        bfs = deque([(start, 0)])
        while bfs:
            (x, y), steps = bfs.popleft()
            if (x, y) == end:
                return True
            for dx, dy in N4:
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y and (nx, ny) not in block:
                    bfs.append(((nx, ny), steps + 1))
                    block.add((nx, ny))
        return False
    
    # You could also use binary search here, but I'm too lazy to implement it and this works fine.
    for n in range(1, len(map)):
        if not travel(n):
            wall = map[n - 1]
            print(f"{wall[0]},{wall[1]}")
            break

    # return data


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
