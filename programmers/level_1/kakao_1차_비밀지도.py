def solution(n, arr1, arr2):
    answer = []
    map_1 = []
    map_2 = []

    for x in arr1:
        r = format(x, 'b').zfill(n)
        map_1.append(r)

    for y in arr2:
        r = format(y, 'b').zfill(n)
        map_2.append(r)

    for i in range(n):
        result = ''
        for j in range(n):
            if map_1[i][j] == '1' or map_2[i][j] == '1':
                result += "#"
            else:
                result += " "

        answer.append(result)

    return answer


if __name__ == '__main__':
    test = [
        [5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
        [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]

    ]

    for a, b, c in test:
        print(solution(a, b, c))
