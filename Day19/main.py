from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    patterns, towels = data
    patterns = set(patterns.split(", "))

    @cache
    def check_towel(towel):
        if towel == "":
            return 1
        
        tot = 0
        for pat in patterns:
            if towel.startswith(pat):
                if x := check_towel(towel[len(pat):]):
                    tot += x
        return tot
    
    return sum(check_towel(towel) for towel in towels)


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
