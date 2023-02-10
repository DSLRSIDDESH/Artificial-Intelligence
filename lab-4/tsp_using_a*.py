inf = float("inf")
graph = [
    [inf, 12, 10, 19, 8],
    [12, inf, 3, 7, 6],
    [10, 3, inf, 2, 20],
    [19, 7, 2, inf, 4],
    [8, 6, 20, 4, inf]
]

def cost_of_mst(graph, n):
    mst_cost,mst_edges = 0,[]
    visited = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            mst_edges.append((graph[i][j], i, j))
    mst_edges.sort()
    for i in mst_edges:
        cost, v1, v2 = i
        if not visited[v1] or not visited[v2]:
            mst_cost += cost
            visited[v1] = visited[v2] = 1
            for j in range(n):
                if (visited[v1] == True or visited[v2] == True):
                    visited[j] = 1
                else:
                    visited[j] = 0
    return mst_cost

def a_star_for_tsp(graph, n, node):
    min_path, min_cost = [node], 0
    mst_cost = cost_of_mst(graph, n)
    visited = [0] * n
    visited[node] = 1
    for i in range(n-1):
        heuristic_value = inf
        next_node = -1
        current_node = min_path[-1]
        for j in range(n):
            if not visited[j]:
                est_cost = min_cost + graph[current_node][j] - mst_cost
                if est_cost < heuristic_value:
                    heuristic_value = est_cost
                    next_node = j
        min_path.append(next_node)
        min_cost += graph[current_node][next_node]
        visited[next_node] = 1
    return min_cost, min_path

min_cost, min_path = a_star_for_tsp(graph, len(graph), 0)
print("Minimum cost:", min_cost + graph[min_path[-1]][0])
print("Minimum cost's Path:", * (min_path + [0]))