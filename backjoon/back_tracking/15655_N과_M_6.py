from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

data = combinations(data, M)

for i, item in enumerate(data):
    # print(i + 1, end = '\t')
    for d in item:
        print(d, end = ' ')
    print()

"""
3 1
4 5 2

2
4
5
-----------------------------
4 2
9 8 7 1

1 7
1 8
1 9
7 8
7 9
8 9
-----------------------------
4 4
1231 1232 1233 1234

1231 1232 1233 1234
"""
