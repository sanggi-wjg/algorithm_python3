import re


def solution(N):
    N = str(format(N, 'b'))
    print(N, type(N))

    # 정규식
    result = re.findall("[1]?(0+)[1]", N)
    print(result)
    if not result:
        return 0

    return len(max(result, key = len))


if __name__ == '__main__':
    print(solution(1), end = '\n\n')
    print(solution(4), end = '\n\n')
    print(solution(9), end = '\n\n')
    print(solution(561), end = '\n\n')
    print(solution(1038), end = '\n\n')
    print(solution(1041), end = '\n\n')
    print(solution(10410), end = '\n\n')
