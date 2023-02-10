from collections import deque
infi = float('inf')

def dfs_for_tsp(graph, u, node, min_path, path, visited):
    visited[u] = 1
    min_path.append(u)
    if len(min_path) == n:
        path[0] = min_path
        return node + graph[u][0]
    min_cost = infi
    for i in range(len(graph)):
        if not visited[i]:
            new_d = node + graph[u][i]
            min_cost = min(min_cost, dfs_for_tsp(graph, i, new_d, min_path.copy(), path, visited))
    return min_cost

def bfs_for_tsp(graph, node, n):
    queue = deque([(0, node, [node])])
    while queue:
        (min_cost, j, min_path) = queue.popleft()
        if len(min_path) == n:
            return (min_cost + graph[j][node],min_path + [node])
        for i in range(n):
            if i not in min_path:
                queue.append((min_cost + graph[j][i], i, min_path + [i]))
    return (infi, 'No Path Found!')

def ids_for_tsp(graph, u, v, node):
    if node + graph[u][0] > infi:
        return infi
    if v == (1 << len(graph)) - 1:
        return node + graph[u][0]
    min_cost = infi
    for i in range(len(graph)):
        if v & (1 << i) == 0:
            min_cost = min(min_cost, ids_for_tsp(graph, i, v | (1 << i), node + graph[u][i]))
    return min_cost

graph = [
            [infi,12,10,19,8],
            [12,infi,3,7,6],
            [10,3,infi,2,20],
            [19,7,2,infi,4],
            [8,6,20,4,infi]
        ]

n = len(graph)
print("Minimum cost (BFS) :", bfs_for_tsp(graph, 0, n)[0])
print("Minimum cost (DFS) :", dfs_for_tsp(graph, 0, 0, [], [None], [0]*n))
print("Minimum cost (IDS) :", ids_for_tsp(graph, 0, 1, 0))
print("Minimum cost's path :", *bfs_for_tsp(graph, 0, len(graph))[1])