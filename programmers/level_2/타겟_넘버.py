def solution(numbers: list, target: int):
    parent_node = [0]

    for n in numbers:
        child_nodes = []

        for node in parent_node:
            child_nodes.append(node + n)
            child_nodes.append(node - n)

        parent_node = child_nodes

        # print(parent_node, child_nodes)

    return parent_node.count(target)


test = [
    [[1, 1, 1, 1, 1], 3, ],
]

for a, b in test:
    ans = solution(a, b)
    print(ans)
