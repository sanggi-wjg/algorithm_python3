from itertools import product

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

data = list(set(product(data, repeat = M)))
data.sort()

for item in data:
    for d in item:
        print(d, end = ' ')
    print()
