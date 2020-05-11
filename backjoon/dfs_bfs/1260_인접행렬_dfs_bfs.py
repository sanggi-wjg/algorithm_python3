import collections
from pprint import pprint


def dfs(matrix: list, visited: list, node: int):
    visited[node] = True
    print('dfs : ', node, visited)

    for i in range(1, len(matrix), 1):
        if matrix[node][i] == 1 and not visited[i]:
            dfs(matrix, visited, i)


def bfs(matrix: list, visited: list, node: int):
    queue = collections.deque()
    queue.append(node)
    visited[node] = True

    while queue:
        v = queue.popleft()
        print('bfs : ', v, visited)

        for i in range(1, len(matrix), 1):
            if matrix[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    MATRIX = [[0] * (N + 1) for _ in range(N + 1)]
    VISITED = [False for _ in range(N + 1)]
    # pprint(MATRIX)

    for _ in range(M):
        a, b = map(int, input().split())
        MATRIX[a][b] = 1
        MATRIX[b][a] = 1

    # pprint(MATRIX)
    dfs(MATRIX, VISITED, V)
    print()

    VISITED = [False for _ in range(N + 1)]
    bfs(MATRIX, VISITED, V)
