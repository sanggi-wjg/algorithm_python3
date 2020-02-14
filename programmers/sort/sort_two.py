def solution(numbers):
    answer = ''
    res = []

    for n in numbers:
        res.append([str(n), str(n) * int(12 / len(str(n)))])
    res = sorted(res, key = lambda x: x[1], reverse = True)

    for o, r in res:
        answer += str(o)

    return str(int(answer))


if __name__ == '__main__':
    ans = solution([3, 6, 9])
    print(ans)
    ans = solution([6, 10, 2])
    print(ans)
    ans = solution([3, 33, 30, 34, 5, 9])
    print(ans)
    ans = solution([3, 33, 30, 34, 5, 9, 100, 110])
    print(ans)
    ans = solution([0, 0, 0, 0, 0])
    print(ans)
