from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    tot_cost = 0
    for machine in data:
        btnA_dx, btnA_dy = tuple(ints(machine[0]))
        btnB_dx, btnB_dy = tuple(ints(machine[1]))
        prize_x, prize_y = tuple(ints(machine[2]))
        prize_x += 10000000000000
        prize_y += 10000000000000
        print(btnA_dx, btnA_dy, btnB_dx, btnB_dy, prize_x, prize_y)

        # Solve the system of equations
        num_A = ((prize_y * btnB_dx) - (prize_x * btnB_dy)) / ((btnB_dx * btnA_dy) - (btnA_dx * btnB_dy))
        num_B = ((prize_x * btnA_dy) - (prize_y * btnA_dx)) / ((btnB_dx * btnA_dy) - (btnA_dx * btnB_dy))
        
        # If solution
        if num_A == int(num_A) and num_B == int(num_B):
            # Add the cost
            tot_cost += int(num_A * 3 + num_B * 1)

    return tot_cost


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
