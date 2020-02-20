def solution(phone_number):
    answer = ''
    idx = 0
    for p in phone_number:
        if len(phone_number) - 4 <= idx:
            answer += p
        else:
            answer += "*"
        idx += 1

    return answer


def solution_2(phone_number):
    answer = ''

    return answer


if __name__ == '__main__':
    ans = solution("01033334444")
    print(ans)
    ans = solution("027778888")
    print(ans)

    ans = solution_2("01033334444")
    print(ans)
    ans = solution_2("027778888")
    print(ans)
