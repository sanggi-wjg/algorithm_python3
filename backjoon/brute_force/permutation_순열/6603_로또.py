from itertools import permutations

if __name__ == '__main__':
    while True:
        case = list(map(int, input().split()))
        N, num = case[0], case[1:]

        if N == 0:
            break

        permuted_data = permutations(num, 6)
        permuted_data = set(map(lambda x: tuple(sorted(x)), permuted_data))
        permuted_data = sorted(permuted_data)

        for r in permuted_data:
            print(' '.join(map(str, r)))

        print()
