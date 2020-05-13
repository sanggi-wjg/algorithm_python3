def permutation(data, i):
    if i == len(data) - 1:
        print(data)

    else:
        for j in range(i, len(data)):
            data[i], data[j] = data[j], data[i]
            permutation(data, i + 1)
            data[i], data[j] = data[j], data[i]


if __name__ == '__main__':
    permutation([1, 2, 3], 0)
