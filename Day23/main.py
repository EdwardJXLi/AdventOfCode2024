from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!
    conn = defaultdict(list)

    for line in data:
        a, b = line.split('-')
        conn[a].append(b)
        conn[b].append(a)

    nodes = list(conn.keys())
    best_clique = set()

    def dfs(current_clique, candidates):
        nonlocal best_clique
        
        if not candidates:
            if len(current_clique) > len(best_clique):
                best_clique = current_clique
            return
        
        for node in list(candidates):
            dfs(current_clique | {node}, candidates & set(conn[node]))
            candidates.remove(node)
    
    dfs(set(), set(nodes))
    
    return ",".join(sorted(best_clique))


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

