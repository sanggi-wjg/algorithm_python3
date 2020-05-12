def solution(X: int, A: list):
    n, count = 0, 0

    while count <= X:
        n = A[count]
        count += n
        print(n, count)

    return A.index(n)


if __name__ == '__main__':
    sample = [
        [[1, 3, 1, 4, 2, 3, 5, 4], 5]
    ]

    for a, b in sample:
        ans = solution(b, a)
        print('Answer:', ans)
