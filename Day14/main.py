from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    # Demo data
    # X = 11
    # Y = 7

    # Input data
    X = 101
    Y = 103

    def print_robots(robots):
        for y in range(Y):
            for x in range(X):
                count = 0
                for px, py, _, _ in robots:
                    if px == x and py == y:
                        count += 1
                if count == 0:
                    print(".", end="")
                else:    
                    print(str(count), end="")
            print()

    # Get robots
    robots = []
    for line in data:
        px, py, vx, vy = ints(line)
        robots.append((px, py, vx, vy))

    THRESHOLD = 0.5

    # Move robots
    iteration = 0
    while True:
        for r in range(len(robots)):
            px, py, vx, vy = robots[r]
            robots[r] = ((px + vx) % X, (py + vy) % Y, vx, vy)
        iteration += 1

        # Count quadrants
        q1 = q2 = q3 = q4 = 0
        for px, py, _, _ in robots:
            if X//2 + 1 <= px < X and 0 <= py < Y//2:
                q1 += 1
            elif 0 <= px < X//2 and 0 <= py < Y//2:
                q2 += 1
            elif 0 <= px < X//2 and Y//2 + 1 <= py < Y:
                q3 += 1
            elif X//2 + 1 <= px < X and Y//2 + 1 <= py < Y:
                q4 += 1

        # I actually dunno if this holds true for all cases, but I just assumed it does because it reuses code from part 1.
        if q1 > THRESHOLD * len(robots) or q2 > THRESHOLD * len(robots) or q3 > THRESHOLD * len(robots) or q4 > THRESHOLD * len(robots):
            print_robots(robots)
            break

    return iteration


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
