def solution(n: int, computers: list):
    conn = dict()

    for no, c in enumerate(computers):
        for i in range(n):
            if c[i] == 1:
                if no not in conn.keys():
                    conn.setdefault(no, { no, i })
                else:
                    conn[no].add(no)
                    conn[no].add(i)

    visited = dfs(conn, 0)
    # print(conn, " | ", visited)

    return (1 + n) - len(visited)


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited


test = [
    [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],
    # [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]],
    [4, [[1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]]],
]

for a, b in test:
    ans = solution(a, b)
    print(ans)
