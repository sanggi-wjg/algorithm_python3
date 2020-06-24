import sys

data = {
    '2': [2, 4, 8, 6],
    '3': [3, 9, 7, 1],
    '4': [4, 6],
    '7': [7, 9, 3, 1],
    '8': [8, 4, 2, 6],
    '9': [9, 1]
}


def solution(a, b):
    num = str(a)[-1]

    if num in ['0', '1', '5', '6']:
        return int(num)
    else:
        d = data.get(num)
        return d[b % len(d) - 1]


T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = solution(a, b)
    sys.stdout.writelines(str(result))
