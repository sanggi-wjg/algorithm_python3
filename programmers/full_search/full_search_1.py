def solution(answers):
    answer = []
    type_1 = [1, 2, 3, 4, 5]
    type_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    type_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = { '1': 0, '2': 0, '3': 0 }

    for n, a in enumerate(answers):
        if a == type_1[n % len(type_1)]:
            count.__setitem__('1', count.get('1') + 1)
        if a == type_2[n % len(type_2)]:
            count.__setitem__('2', count.get('2') + 1)
        if a == type_3[n % len(type_3)]:
            count.__setitem__('3', count.get('3') + 1)

    sortCount = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
    print(count)
    print(sortCount)

    cmp = 0
    for k, v in sortCount.items():
        if v >= cmp:
            answer.append(int(k))
            cmp = v

    if not answer:
        return [1, 2, 3]

    return answer


if __name__ == '__main__':
    testData = [
        [1, 2, 3, 4, 5],
        [1, 3, 2, 4, 2],
        [3, 3, 3, 4, 1, 1, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [5, 5, 5, 5, 3],
    ]

    for test in testData:
        ans = solution(test)
        print(ans, end = '\n\n')
