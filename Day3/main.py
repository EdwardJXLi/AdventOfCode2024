from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    data = "\n".join(data)
    do = True
    tot = 0
    
    while data:
        if data.startswith("do()"):
            data = data[3:]
            do = True
            continue
        elif data.startswith("don't()"):
            data = data[6:]
            do = False
            continue
        elif data.startswith("mul("):
            if ")" in data:
                args = data[4:].split(")", 1)[0]
                if args.count(",") == 1:
                    x, y = args.split(",")
                    if x.isdigit() and y.isdigit():
                        if do:
                            tot += int(x) * int(y)
                            data = data[4:].split(")", 1)[1]
                            continue
        data = data[1:]

    return tot


if __name__ == "__main__":
    # LEGACY INPUT PARSING
    # ================================
    if (res := run(get_input(split=None, auto_zero_index=False))) is not None:
        print(res)
    # ================================

    # NEW INPUT PARSING
    # ================================
    # TODO
    # ================================
