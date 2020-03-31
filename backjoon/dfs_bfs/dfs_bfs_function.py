import collections


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            print('Visit : ', n, ' Visited : ', visited, ' Stack : ', stack)

    return visited


def bfs(graph, root):
    visited = []
    queue = collections.deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
            print('Visit : ', n, ' Visited : ', visited, ' Queue : ', queue)

    return visited


if __name__ == '__main__':
    graph_list = {
        1: { 3, 4 },
        2: { 3, 4, 5 },
        3: { 1, 5 },
        4: { 1 },
        5: { 2, 6 },
        6: { 3, 5 },
    }
    print(type(graph_list), graph_list, type(graph_list[1]))
    root_node = 1

    print('DFS')
    dfs(graph_list, root_node)
    print('\nBFS')
    bfs(graph_list, root_node)
