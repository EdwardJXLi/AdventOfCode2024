from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    world, X, Y = single_char_grid(data)

    DIRECTION = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    # Get starting position
    for y in range(Y):
        for x in range(X):
            if world[y][x] == "S":
                start = (x, y)
                world[y][x] = "."
            if world[y][x] == "E":
                end = (x, y)
                world[y][x] = "."

    queue = []
    heapq.heappush(queue, (0, start[0], start[1], 0, {(start[0], start[1])}))

    tot = set()
    best = INF
    visited = dict()
    while queue:
        score, x, y, direction, nodes = heapq.heappop(queue)
        if (x, y, direction) in visited:
            old_score = visited[(x, y, direction)]
            if score > old_score:
                continue
        visited[(x, y, direction)] = score

        if (x, y) == end:
            if score < best:
                best = score
                tot = copy(nodes)
                print(score, nodes)
            elif score == best:
                tot |= nodes
                print(score, nodes)
            else:
                print(score, nodes)
                break

        heapq.heappush(queue, (score+1000, x, y, (direction+1)%4, nodes))
        heapq.heappush(queue, (score+1000, x, y, (direction-1)%4, nodes))

        dx, dy = DIRECTION[direction]
        nx, ny = x + dx, y + dy
        if world[ny][nx] == ".":
            new_nodes = copy(nodes)
            new_nodes.add((nx, ny))
            heapq.heappush(queue, (score+1, nx, ny, direction, new_nodes))
    
    # for x, y in tot:
    #     world[y][x] = "O"
    # print_grid(world)
    return len(tot)


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
