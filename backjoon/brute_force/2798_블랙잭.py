from itertools import permutations


def find(data, find_value):
    data = sorted(data)
    before, current = 0, 0

    if find_value in data:
        return find_value

    for d in data:
        current = d

        if current > find_value:
            return before

        before = current

    return current


N, M = map(int, input().split())
cards = list(map(int, input().split()))

permuted_data = permutations(cards, 3)
permuted_data = list(set(map(lambda x: tuple(sorted(x)), permuted_data)))
# permuted_data = sorted(permuted_data)

# print(permuted_data)
psum = []

for p in permuted_data:
    psum.append(p[0] + p[1] + p[2])

# print(sorted(psum))
print(find(psum, M))
