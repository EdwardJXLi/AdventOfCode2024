from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    d1, d2 = data

    old_world, X, Y = single_char_grid(d1)
    ins = "".join(d2)

    world = []
    for y in range(Y):
        world.append([])
        for x in range(X):
            if old_world[y][x] == ".":
                world[y].append(".")
                world[y].append(".")
            elif old_world[y][x] == "#":
                world[y].append("#")
                world[y].append("#")
            elif old_world[y][x] == "O":
                world[y].append("[")
                world[y].append("]")
            elif old_world[y][x] == "@":
                world[y].append("@")
                world[y].append(".")
            else:
                world[y].append("??")

    X *= 2
    
    # Find position of player
    player = (0, 0)
    for y in range(Y):
        for x in range(X):
            if world[y][x] == "@":
                player = (x, y)

    def try_push(x, y, direction, tried):
        if (x, y) in tried:
            return True
        tried.add((x, y))
        dx, dy = direction
        if world[y][x] == ".":
            return True
        elif world[y][x] == "#":
            return False
        # elif world[y][x] == "O":
        #     can_move = try_push(x + dx, y + dy, direction)
        #     if can_move:
        #         world[y + dy][x + dx] = "O"
        #         world[y][x] = "."
        #         return True
        #     else:
        #         return False
        elif world[y][x] == "@":
            can_move = try_push(x + dx, y + dy, direction, tried)
            if can_move:
                world[y + dy][x + dx] = "@"
                world[y][x] = "."
                return True
            else:
                return False
        elif (world[y][x] == "[" or world[y][x] == "]") and direction[1] == 0:
            can_move = try_push(x + dx, y + dy, direction, tried)
            if can_move:
                world[y + dy][x + dx] = world[y][x]
                world[y][x] = "."
                return True
            else:
                return False
        elif world[y][x] == "[" and direction[0] == 0:
            can_move = try_push(x+1, y, direction, tried) and try_push(x + dx, y + dy, direction, tried)
            if can_move:
                world[y + dy][x + dx] = world[y][x]
                world[y][x] = "."
                return True
            else:
                return False
        elif world[y][x] == "]" and direction[0] == 0:
            can_move = try_push(x-1, y, direction, tried) and try_push(x + dx, y + dy, direction, tried)
            if can_move:
                world[y + dy][x + dx] = world[y][x]
                world[y][x] = "."
                return True
            else:
                return False
        return False
            
    def print_world():
        for y in range(Y):
            for x in range(X):
                print(world[y][x], end="")
            print()
        print()
            
    for i in ins:
        undo = deepcopy(world)
        if i == "^":
            direction = (0, -1)
        elif i == "v":
            direction = (0, 1)
        elif i == "<":
            direction = (-1, 0)
        elif i == ">":
            direction = (1, 0)
        
        x, y = player
        dx, dy = direction
        can_move = try_push(x, y, direction, set())
        if can_move:
            player = (x + dx, y + dy)
        else:
            world = undo

    score = 0

    for y in range(Y):
        for x in range(X):
            if world[y][x] == "[":
                score += (100 * y + x)

    print_world()

    return score


if __name__ == "__main__":
    # LEGACY INPUT PARSING
    # ================================
    if (res := run(get_input(split="\n\n", auto_zero_index=False))) is not None:
        print(res)
    # ================================

    # NEW INPUT PARSING
    # ================================
    # TODO
    # ================================
