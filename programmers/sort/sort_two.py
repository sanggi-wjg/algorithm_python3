def solution(numbers):
    answer = ''
    res = dict()

    for n in numbers:
        res.__setitem__(str(n), str(n)[0])

    print(res)
    res = sorted(res.items(), key = lambda x: x[1], reverse = True)
    print(res)
    res.sort(reverse = True)
    print(res)

    return answer


if __name__ == '__main__':
    ans = solution([3, 6, 9])
    print(ans)

    ans = solution([6, 10, 2])
    print(ans)

    ans = solution([3, 33, 30, 34, 5, 9])
    print(ans)
