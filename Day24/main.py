from aoc_utils import *


def run(data: str | list[str] | list[list[str]]):
    # Lets do this!

    # ===== PART 1 =====
    bits = defaultdict(int)
    graph = defaultdict(list)

    for imp in data[0]:
        addr, dat = imp.split(": ")
        bits[addr] = int(dat)
        graph[addr] = []

    for ins in data[1]:
        a, op, b, _, c = ins.split()
        if op == "AND":
            graph[c].append(("AND", a, b))
        elif op == "OR":
            graph[c].append(("OR", a, b))
        elif op == "XOR":
            graph[c].append(("XOR", a, b))

    def get_value(addr):
        if addr in bits:
            return bits[addr]
        elif addr in graph:
            op, a, b = graph[addr][0]
            if op == "AND":
                return get_value(a) & get_value(b)
            elif op == "OR":
                return get_value(a) | get_value(b)
            elif op == "XOR":
                return get_value(a) ^ get_value(b)
            else:
                return None
        else:
            return None

    num = 0

    for i in range(99):
        addr = f"z{i:02}"
        val = get_value(addr)
        print(addr, val)
        if val is not None:
            num += val * (2 ** i)
        else:
            break

    print("Part 1:", num)

    # ===== PART 2 =====
    # Part 2 I ended up generating a graph of the circuit and then solving it by hand.
    # Sorry no automated solution for this one. :(
    
    import graphviz as dot

    g = dot.Digraph(graph_attr={"rankdir": "LR"})

    # for bit in bits.keys():
    #     g.node(bit)

    for ins in data[1]:
        a, op, b, _, c = ins.split()
        
        if op == "OR":
            continue

        id = "_".join([a, op, b])
        g.node(id, op, shape="box")
        g.edge(a, id)
        g.edge(b, id)
        g.edge(id, c)
    
    g.render("graph.png")



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
