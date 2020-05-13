def permutation(data, i, res):
    if i == len(data) - 1:
        # print(' '.join(map(str, data)))
        res.append(' '.join(map(str, data)))

    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1, res)
            data[i], data[j] = data[j], data[i]

    return res


def main1():
    N, result = int(input()), []
    permutation([i for i in range(1, N + 1)], 0, result)
    # print(result)
    result = sorted(result)
    for r in result:
        print(r)


def main2():
    from itertools import permutations

    N = int(input())
    result = permutations([i for i in range(1, N + 1)])
    for r in result:
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    main2()
