from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    data = list(map(int, input().split()))

    result = []
    permute_data = permutations(data)
    for p in permute_data:
        temp = 0
        # print(p)
        for i in range(len(p) - 1):
            temp += abs(p[i] - p[i + 1])
            # print(p[i], '-', p[i + 1], '=', abs(p[i] - p[i + 1]))

        result.append(temp)

    # print(result)
    print(max(result))
