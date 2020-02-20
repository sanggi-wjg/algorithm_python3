def solution(answers):
    answer = []
    type_1 = [1, 2, 3, 4, 5]
    type_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    type_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    total = dict()

    for n, a in enumerate(answers):
        if a == type_1[n % len(type_1)]:
            if '1' in total.keys():
                total.__setitem__('1', total.get('1') + 1)
            else:
                total.setdefault('1', 1)
        if a == type_2[n % len(type_2)]:
            if '2' in total.keys():
                total.__setitem__('2', total.get('2') + 1)
            else:
                total.setdefault('2', 1)
        if a == type_3[n % len(type_3)]:
            if '3' in total.keys():
                total.__setitem__('3', total.get('3') + 1)
            else:
                total.setdefault('3', 1)

    print('origin: ', total)
    total = dict(sorted(total.items(), key = lambda x: x[1], reverse = True))
    print('sorted: ', total)

    for k, v in total.items():
        answer.append(int(k))

    if not answer:
        return [1, 2, 3]

    return answer


if __name__ == '__main__':
    ans = solution([1, 2, 3, 4, 5])
    print(ans)
    print()

    ans = solution([1, 3, 2, 4, 2])
    print(ans)
    print()

    ans = solution([3, 3, 3, 4, 1, 1, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    print(ans)
    print()

    ans = solution([5, 5, 5, 5, 3])
    print(ans)
    print()
