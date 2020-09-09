from itertools import combinations_with_replacement

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

data = list(set(combinations_with_replacement(data, M)))
data.sort()

for item in data:
    for d in item:
        print(d, end = ' ')
    print()
