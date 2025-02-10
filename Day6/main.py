from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    sg = sparse_grid(data, true=["#", "^"], keepVal=True)

    world = set((x, y) for x, y, c in sg if c == "#")
    start_x, start_y = next((x, y) for x, y, c in sg if c == "^")

    min_x = min(x for x, y in world)
    max_x = max(x for x, y in world)
    min_y = min(y for x, y in world)
    max_y = max(y for x, y in world)

    fucked = set()

    for block_x in range(min_x, max_x+1):
        for block_y in range(min_y, max_y+1):
            locs = set()
            direction = (0, -1)
            px, py = start_x, start_y

            while min_x <= px <= max_x and min_y <= py <= max_y:
                # print(px, py)
                nx, ny = px + direction[0], py + direction[1]
                if (nx, ny) in world or (nx, ny) == (block_x, block_y):
                    if direction == (0, -1):
                        direction = (1, 0)
                    elif direction == (1, 0):
                        direction = (0, 1)
                    elif direction == (0, 1):
                        direction = (-1, 0)
                    elif direction == (-1, 0):
                        direction = (0, -1)
                else:
                    px, py = nx, ny
                    if (px, py, direction) in locs:
                        break
                    locs.add((px, py, direction))
            else:
                continue

            fucked.add((block_x, block_y))

    return len(fucked)


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
