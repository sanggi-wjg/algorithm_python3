import collections


def dfs(graph, root):
    visited = []
    stack = [root]
    if root not in graph.keys():
        return [root]

    while stack:
        n = stack.pop()
        # print('n:', n, 'stack : ', stack)

        if n not in visited:
            visited.append(n)
            temp = list(graph[n] - set(visited))
            temp.sort(reverse = True)
            stack += temp
            # print('Visit : ', n, ' Visited : ', visited, ' Stack : ', stack)

    return visited


def bfs(graph, root):
    visited = []
    queue = collections.deque([root])

    if root not in graph.keys():
        return [root]

    while queue:
        n = queue.popleft()
        # print('n:', n, 'queue : ', queue)

        if n not in visited:
            visited.append(n)
            temp = list(graph[n] - set(visited))
            temp.sort()
            queue += temp
            # print('Visit : ', n, ' Visited : ', visited, ' Queue : ', queue)

    return visited


N, M, V = map(int, input().split())
G = dict()

for i in range(M):
    a, b = map(int, input().split())
    G.setdefault(a, { b }) if a not in G.keys() else G[a].add(b)
    G.setdefault(b, { a }) if b not in G.keys() else G[b].add(a)
# print(G)

result = dfs(G, V)
for i in range(len(result)):
    print(result[i], end = ' ')
print()

result = bfs(G, V)
for i in range(len(result)):
    print(result[i], end = ' ')
