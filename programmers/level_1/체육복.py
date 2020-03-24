def solution(n: int, lost: list, reserve: list):
    answer = n
    temp = list()

    for lo in lost:
        if lo in reserve:
            reserve.remove(lo)
            temp.append(lo)

    for t in temp:
        lost.remove(t)

    for r in reserve:
        # print('reserve', r, lost, reserve)
        if r - 1 in lost:
            lost.remove(r - 1)

        elif r + 1 in lost:
            lost.remove(r + 1)

        # print('after', lost, reserve)

    return answer - len(lost)


if __name__ == '__main__':
    test = [
        [5, [2, 4], [1, 3, 5]],
        [5, [2, 4], [3]],
        [3, [3], [1]],
        [10, [3, 9, 10], [3, 8, 9]],
    ]

    for a, b, c in test:
        print(solution(a, b, c))
