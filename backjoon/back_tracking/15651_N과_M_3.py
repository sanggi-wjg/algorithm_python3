from itertools import permutations

N, M = 4, 2

data = [n + 1 for n in range(N)]
data = permutations(data, M)
# data = set(data)
print(list(data))
