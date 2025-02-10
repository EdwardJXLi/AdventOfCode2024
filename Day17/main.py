from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    A_orig = ints(data[0])[0]
    B_orig = ints(data[1])[0]
    C_orig = ints(data[2])[0]
    program_orig = ints(data[4])

    # print(A_orig, B_orig, C_orig, program_orig)

    # Initial CPU Emulator
    def run_emu(A, B, C, program):
        pc = 0
        out = []

        def get_combo(operand):
            if 0 <= operand <= 3:
                return operand
            elif operand == 4:
                return A
            elif operand == 5:
                return B
            elif operand == 6:
                return C
            else:
                raise ValueError(f"Invalid operand: {operand}")

        while pc < len(program):
            ins = program[pc]
            pc += 1
            operand = program[pc]

            if ins == 0:  # adv
                A = A // 2**get_combo(operand)
            elif ins == 1:  # bxl
                B = B ^ operand
            elif ins == 2:  # bst
                B = get_combo(operand) % 8
            elif ins == 3:  # jnz
                if A != 0:
                    pc = operand
                    pc -= 1
            elif ins == 4:  # bxc
                B = B ^ C
            elif ins == 5:  # out
                out.append(get_combo(operand) % 8)
                print("out:", get_combo(operand) % 8)
            elif ins == 6:
                B = A // 2**get_combo(operand)
            elif ins == 7:
                C = A // 2**get_combo(operand)
            
            pc += 1

        return out
    
    print(run_emu(A_orig, B_orig, C_orig, program_orig))
    
    # Decompiled CPU Emulator
    def run_decompile(A, B, C):
        out = []
        while True:
            B = A % 8
            B = B ^ 3
            C = A // (2 ** B)
            A = A // (2 ** 3)
            B = B ^ C
            B = B ^ 5
            print(B % 8)
            if A == 0:
                break
        return out
            
        # 2  B = A % 8 
        # 4  .
        # 1  B = B ^ 3
        # 3  .
        # 7  C = A // (2 ** B)
        # 5  .
        # 0  A = A // (2 ** 3)
        # 3  .
        # 4  B = B ^ C
        # 3  .
        # 1  B = B ^ 5
        # 5  .
        # 5  print B % 8
        # 5  .
        # 3  if A == 0:
        # 0    break

    # print(run_decompile(A_orig, B_orig, C_orig))

    # Optimized Decompiled CPU Emulator
    def run_decompile_2(A):
        A_last3 = A % 8
        A_rest = A >> 3
        B = (A_last3 ^ 3) ^ A // (2 ** (A_last3 ^ 3)) ^ 5
        print(B % 8)
        A = A_rest
        if A != 0:
            run_decompile_2(A)

    # run_decompile_2(A_orig)

    # 2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0

    # Backwards value solver
    def backsolve(target, idx, A_rest):
        # print(idx, A_rest)
        if idx < 0:
            return A_rest
        for A_last3 in range(8):
            A = A_rest * 8 + A_last3
            B = (A_last3 ^ 3) ^ A // (2 ** (A_last3 ^ 3)) ^ 5
            # print("check", A, "B", B)
            if B % 8 == target[idx]:
                if ret := backsolve(target, idx - 1, A):
                    return ret
        return None
    
    # Solve
    print(backsolve(program_orig, len(program_orig) - 1, 0))


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
