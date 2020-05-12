def solution(n: int, computers: list):
    graph = { }
    result = []

    for i, computer in enumerate(computers):
        for j, c in enumerate(computer):
            if c == 1:
                graph.setdefault(i, { j }) if i not in graph.keys() else graph[i].add(j)

    for i in range(len(graph)):
        result.append(dfs(graph, i))

    result = list(set(map(tuple, result)))

    # print(computers, ' | ', graph, ' | ', result)
    return len(result)


def dfs(graph, root_node):
    visited = []
    stack = [root_node]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return sorted(visited)


test = [
    [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
    [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
]

ANSWER = [
    2, 1
]

for a, b in test:
    ans = solution(a, b)
    print(ans)
