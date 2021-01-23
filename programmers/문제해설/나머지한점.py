import collections


def solution(points):
    x, y = [], []

    for p in points:
        x.append(p[0])
        y.append(p[1])

    x, y = collections.Counter(x), collections.Counter(y)

    return [x.most_common(2)[1][0], y.most_common(2)[1][0]]


sample = [
    [[1, 4], [3, 4], [3, 10]],  # [1, 10]
    [[1, 1], [2, 2], [1, 2]],  # [2, 1]
]

for s in sample:
    a = solution(s)
    print(a)
