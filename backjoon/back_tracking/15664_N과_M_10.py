from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

data = list(set(combinations(data, M)))
data.sort()

for item in data:
    for d in item:
        print(d, end = ' ')
    print()
"""
3 1
4 4 2

2
4
------------------------------
4 2
9 7 9 1

1 7
1 9
7 9
9 9
------------------------------
4 4
1 1 2 2

1 1 2 2
"""
