from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    world, X, Y = single_char_grid(data)

    # Get starting position
    for y in range(Y):
        for x in range(X):
            if world[y][x] == "S":
                start = (x, y)
                world[y][x] = "."
            if world[y][x] == "E":
                end = (x, y)
                world[y][x] = "."

    # Backwards floodfill
    path_cost = dict()
    queue = []
    cur_cost = 0
    queue.append((end[0], end[1]))

    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if (x, y) in path_cost:
                continue
            path_cost[(x, y)] = cur_cost
            for dx, dy in NEIGHBORS4:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < X and 0 <= ny < Y and world[ny][nx] == ".":
                    queue.append((nx, ny))
        cur_cost += 1

    max_cost = path_cost[start]

    # Forward floodfill
    queue = []
    cur_cost = max_cost
    visited = set()
    saved = defaultdict(int)
    queue.append((start[0], start[1]))

    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in NEIGHBORS4:
                nx = x + dx
                ny = y + dy
                # nnx = nx + dx
                # nny = ny + dy
                if 0 <= nx < X and 0 <= ny < Y and world[ny][nx] == ".":
                    queue.append((nx, ny))
                
                # if (nx, ny) in path_cost:
                #     old_cost = path_cost[(nx, ny)]
                #     new_cost = cur_cost - 1
                #     saved[new_cost-old_cost] += 1
                #     print("-", x, y, nx, ny, old_cost, new_cost)
                # if (nnx, nny) in path_cost:
                #     old_cost = path_cost[(nnx, nny)]
                #     new_cost = cur_cost - 2
                #     saved[new_cost-old_cost] += 1
                #     print("-", x, y, nnx, nny, old_cost, new_cost)

            cheat_queue = []
            cheat_left = 20 - 1
            cheat_cur_cost = cur_cost - 1
            cheat_visited = {(x, y)}
            for dx, dy in NEIGHBORS4:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < X and 0 <= ny < Y:
                    cheat_queue.append((nx, ny))

            while cheat_queue and cheat_left >= 0:
                for _ in range(len(cheat_queue)):
                    x, y = cheat_queue.pop(0)
                    if (x, y) in cheat_visited:
                        continue
                    cheat_visited.add((x, y))

                    if world[y][x] == ".":
                        old_cost = path_cost[(x, y)]
                        if cheat_cur_cost > old_cost:
                            saved[cheat_cur_cost-old_cost] += 1

                    for dx, dy in NEIGHBORS4:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < X and 0 <= ny < Y:
                            cheat_queue.append((nx, ny))

                cheat_left -= 1
                cheat_cur_cost -= 1
        cur_cost -= 1

    tot = 0
    for s, n in sorted(saved.items(), reverse=True):
        if s >= 100:
            tot += n

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
