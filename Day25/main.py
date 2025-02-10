from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    X = 5
    Y = 7

    keys = []
    locks = []

    for cryptic in data:
        # Lock
        if cryptic[0][0] == "#":
            lock = [0] * X
            for y in range(1, Y):
                for x in range(X):
                    if cryptic[y][x] == "#":
                        lock[x] += 1
            locks.append(lock)
        elif cryptic[0][0] == ".":
            key = [0] * X
            for y in range(Y-2, 0, -1):
                for x in range(X):
                    if cryptic[y][x] == "#":
                        key[x] += 1
            keys.append(key)
        else:
            raise Exception("Invalid cryptic")

    tot = 0
    for lock in locks:
        for key in keys:
            for i in range(X):
                if lock[i] + key[i] > 5:
                    break
            else:
                tot += 1

    return tot


if __name__ == "__main__":
    # LEGACY INPUT PARSING
    # ================================
    if (res := run(get_input(split="\n\n"))) is not None:
        print(res)
    # ================================

    # NEW INPUT PARSING
    # ================================
    # TODO
    # ================================
