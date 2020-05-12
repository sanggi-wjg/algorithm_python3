from pprint import pprint


def dfs(matrix: list, visited: list, node: int):
    visited[node] = True
    print('dfs : ', node, visited)

    for i in range(1, len(matrix), 1):
        if matrix[node][i] == 1 and not visited[i]:
            dfs(matrix, visited, i)


if __name__ == '__main__':
    N = int(input())
    VISITED = [False] * N
    MAP = [[0] * (N + 1)]
    for _ in range(N):
        MAP.append([0] + list(map(int, input())))
    print(VISITED)
    pprint(MAP)

    dfs(MAP, VISITED, 1)
