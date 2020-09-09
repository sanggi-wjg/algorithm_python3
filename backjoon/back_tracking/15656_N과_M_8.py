from itertools import combinations_with_replacement

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

data = combinations_with_replacement(data, M)

for item in data:
    for d in item:
        print(d, end = ' ')
    print()
