from itertools import combinations_with_replacement

N, M = map(int, input().split())

data = combinations_with_replacement([n + 1 for n in range(N)], M)

for item in data:
    for d in item:
        print(d, end = ' ')
    print()
