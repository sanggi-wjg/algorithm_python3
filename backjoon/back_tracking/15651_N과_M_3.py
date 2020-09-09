from itertools import product

N, M = map(int, input().split())

data = [n + 1 for n in range(N)]
result = product(data, repeat = M)

for item in result:
    for r in item:
        print(r, end = ' ')
    print()

"""
3 1 (3)
4 2 (16)
3 3 (27)
4 4 (64)

3 1 (3)
1
2
3

4 2 (16)

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

3 3 (27)

1 1 1
1 1 2
1 1 3
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2
3 2 3
3 3 1
3 3 2
3 3 3

"""
