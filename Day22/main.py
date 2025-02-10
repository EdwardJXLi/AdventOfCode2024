from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    def calc_secret(secret, loop_size):
        out = []
        out.append(secret)
        for _ in range(loop_size):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret // 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
            out.append(secret)
        return out

    scores = defaultdict(int)
    for line in data:
        secrets = calc_secret(int(line), 2000)
        secrets = [s%10 for s in secrets]
        deltas = [secrets[i+1] - secrets[i] for i in range(len(secrets)-1)]

        local_scores = dict()
        for i in range(len(deltas)-3):
            x4s = tuple(deltas[i:i+4])
            xx = secrets[i+4]
            if x4s not in local_scores:
                local_scores[x4s] = xx

        for k, v in local_scores.items():
            scores[k] += v

    return max(scores.values())


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
