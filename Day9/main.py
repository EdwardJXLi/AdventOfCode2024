from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    disk = []
    blocks = []

    # Parse Data
    num = 0
    block = True
    for i in data:
        dlen = int(i)
        if block:
            blocks.append((len(disk), dlen))
            disk += [num] * dlen
            block = False
            num += 1
        else:
            disk += [None] * dlen
            block = True

    # Try to shuffle each block back using sliding window
    for idx, length in reversed(blocks):
        window = 0
        for i in range(length):
            window += disk[i] is not None
        for i in range(len(disk)-length):
            if i >= idx:
                break
            if window == 0:
                # print("FOUND", i)
                disk[i:i+length], disk[idx:idx+length] = disk[idx:idx+length], disk[i:i+length]
                break
            window = window - (disk[i] is not None) + (disk[i+length] is not None)

    # Calculate checksum
    checksum = 0
    for i in range(len(disk)):
        if disk[i] is not None:
            checksum += disk[i] * i

    return checksum


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
