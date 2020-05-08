import collections


def dfs(graph: dict, root: int):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            # print('{} {} {} '.format(n, stack, visited))

    return visited


def bfs(graph: dict, root: int):
    visited = []
    queue = collections.deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited


N = int(input())
C = int(input())
G = dict()

for i in range(C):
    a, b = map(int, input().split())
    G.setdefault(a, { b }) if a not in G.keys() else G[a].add(b)
    G.setdefault(b, { a }) if b not in G.keys() else G[b].add(a)
# print(G)

result = dfs(G, 1)
print(len(result) - 1)

result = bfs(G, 1)
print(len(result) - 1)
