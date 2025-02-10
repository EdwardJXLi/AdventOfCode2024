from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    orders = [tuple(map(int, order.split("|"))) for order in data[0]]
    updates = [list(map(int, update.split(","))) for update in data[1]]
    incorrect = []
    correct = []

    for update in updates:
        ucopy = deepcopy(update)
        while ucopy:
            val = ucopy.pop(0)
            for j, other in enumerate(ucopy):
                if (other, val) in orders:
                    incorrect.append(update)
                    break
                else:
                    pass
            else:
                continue
            break
        else:
            correct.append(update)

    for inc in incorrect:
        for i in range(len(inc)):
            for j in range(i+1, len(inc)):
                if (inc[j], inc[i]) in orders:
                    inc[i], inc[j] = inc[j], inc[i]

    tot = 0
    for i in incorrect:
        tot += i[len(i)//2]
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
