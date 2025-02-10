from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    stones = ints(data)

    @cache
    def dfs(stone, depth):
        if depth == 75:
            return 1
        
        if stone == 0:
            return dfs(1, depth+1)
        elif len(str(stone)) % 2 == 0:
            return dfs(int(str(stone)[0:len(str(stone))//2]), depth+1) + dfs(int(str(stone)[len(str(stone))//2:]), depth+1)
        else:
            return dfs(stone * 2024, depth+1)

    return sum(dfs(s, 0) for s in stones)


if __name__ == "__main__":
    # LEGACY INPUT PARSING
    # ================================
    if (res := run(get_input(auto_zero_index=True))) is not None:
        print(res)
    # ================================

    # NEW INPUT PARSING
    # ================================
    # TODO
    # ================================
