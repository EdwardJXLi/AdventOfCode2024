from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    def solve(idx, nums, so_far, target):
        if idx == len(nums):
            return so_far == target

        return solve(idx + 1, nums, so_far + nums[idx], target) + solve(idx + 1, nums, so_far * nums[idx], target) + solve(idx + 1, nums, int(str(so_far) + str(nums[idx])), target)

    tot = 0
    for line in data:
        target, *rest = ints(line)

        if solve(0, rest, 0, int(target)):
            tot += (target)

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
