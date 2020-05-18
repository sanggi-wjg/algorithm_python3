from itertools import permutations

heights = []

for _ in range(9):
    heights.append(int(input()))

permuted_data = permutations(heights, 7)
permuted_data = set(map(lambda x: tuple(sorted(x)), permuted_data))
permuted_data = sorted(permuted_data)

result = []

for p in permuted_data:
    if sum(p) == 100:
        result = p
        break

for r in result :
    print(r)