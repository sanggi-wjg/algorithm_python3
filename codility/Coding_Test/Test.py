def solution(A):
    A = list(set(A))
    # print(A)

    if max(A) <= 0:
        return 1

    for i in range(1, len(A) + 1):
        if A[i - 1] != i:
            return i

    return max(A) + 1


sample = [
    [-1, -2, 1, 2, 3],
    [-1, -2, -2, 1],
    # [1, 3, 6, 4, 1, 2],
    # [1, 2, 3],
    # [2, 3, 4],
    # [5, 4, 4, 3, 1, 2, 10, 9],
    # [-1, -3],
]

for s in sample:
    # print(s)
    answer = solution(s)
    print(answer)
