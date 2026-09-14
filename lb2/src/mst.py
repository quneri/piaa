INF = float("inf")


def prim_mst(graph, vertices):
    if len(vertices) <= 1:
        return 0


    used = set()

    distance = {v: INF for v in vertices}

    start = vertices[0]
    distance[start] = 0

    result = 0

    while len(used) < len(vertices):

        current = None

        for v in vertices:
            if v not in used:
                if current is None or distance[v] < distance[current]:
                    current = v


        if current is None:
            return INF

        used.add(current)

        result += distance[current]

        for u in vertices:
            if u not in used:
                if graph[current][u] != -1:
                    if graph[current][u] < distance[u]:
                        distance[u] = graph[current][u]

    return result
