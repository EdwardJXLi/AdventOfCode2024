from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    l1 = []
    l2 = []

    for i in data:
        a, b = i.split()
        l1.append(int(a))
        l2.append(int(b))

    tot = 0
    for i in range(len(l1)):
        tot += abs(l1[i] * l2.count(l1[i]))

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
