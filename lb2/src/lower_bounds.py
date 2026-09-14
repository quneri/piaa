from mst import prim_mst


INF = float("inf")


def get_pieces(path, n):
    pieces = []
    pieces.append(path[:])
    visited = set(path)

    for v in range(n):
        if v not in visited:
            pieces.append([v])

    return pieces


def outgoing_edges(piece, pieces, graph):
    result = []
    end = piece[-1]

    for other in pieces:
        if other is piece:
            continue

        start = other[0]
        if graph[end][start] != -1:
            result.append(graph[end][start])

    return result


def incoming_edges(piece, pieces, graph):
    result = []
    start = piece[0]
    for other in pieces:

        if other is piece:
            continue

        end = other[-1]
        if graph[end][start] != -1:
            result.append(graph[end][start])

    return result


def lower_bound_half(graph, path):
    n = len(graph)
    pieces = get_pieces(path, n)
    total = 0

    for piece in pieces:
        out_edges = outgoing_edges(piece, pieces, graph)

        in_edges = incoming_edges(piece, pieces, graph)

        if len(out_edges) == 0:
            return INF

        if len(in_edges) == 0:
            return INF

        out_edges.sort()
        in_edges.sort()

        total += out_edges[0]
        total += in_edges[0]

    return total / 2


def lower_bound_mst(graph, path):
    pieces = get_pieces(path, len(graph))

    if len(pieces) <= 1:
        return 0

    n = len(pieces)
    compressed = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            from_vertex = pieces[i][-1]
            to_vertex = pieces[j][0]
            compressed[i][j] = graph[from_vertex][to_vertex]

    return prim_mst(compressed, list(range(n)))


def calculate_lower_bound(graph, path):
    l1 = lower_bound_half(graph, path)
    l2 = lower_bound_mst(graph, path)
    
    return max(l1, l2)
