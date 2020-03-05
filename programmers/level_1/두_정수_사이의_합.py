def solution(a, b):
    num_sum = lambda x, y: int((x * (x + 1) / 2) - ((y - 1) * ((y - 1) + 1) / 2))
    return num_sum(a, b) if a >= b else num_sum(b, a)


test = [
    [3, 5],
    [3, 3],
    [5, 3],
]

for i, j in test:
    print(solution(i, j))
