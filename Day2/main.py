from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    count = 0
    for row in data:
        nums = ints(row)
        for j in range(len(nums)):
            sub = nums[:j] + nums[j+1:]
            if (sub == sorted(sub) or sub == sorted(sub, reverse=True)) and all(1 <= abs(a - b) <= 3 for a, b in pairwise(sub)):
                count += 1
                break

    return count


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
