import collections


def solution(A):
    counter = collections.Counter(A)
    print(A, counter)

    for c in counter:
        if counter[c] % 2 != 0:
            return c


if __name__ == '__main__':
    sample = [
        [9, 3, 9, 3, 9, 7, 9],
        [1, 2, 1, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 1, 2],
        [1],
        [1, 2, 1],
    ]

    for a in sample:
        ans = solution(a)
        print(ans)
