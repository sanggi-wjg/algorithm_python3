def solution(A, K):
    # print(A)
    # print(A[0:len(A) - K])
    # print(A[len(A) - K: len(A)])
    pre = A[len(A) - K: len(A)]
    post = A[0:len(A) - K]

    return pre + post

    # for i in range(K):
    #     n = A.pop(len(A) - 1)
    #     A.insert(0, n)
    #
    # return A


if __name__ == '__main__':
    sample = [
        # [[3, 8, 9, 7, 6], 1, [6, 3, 8, 9, 7]],
        # [[3, 8, 9, 7, 6], 2, [7, 6, 3, 8, 9]],
        [[3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]],
        # [[1, 2, 3, 4], 1, [4, 1, 2, 3]],
        # [[1, 2, 3, 4], 2, [3, 4, 1, 2]],
        # [[1, 2, 3, 4], 3, [2, 3, 4, 1]],
        [[1, 2, 3, 4], 4, [1, 2, 3, 4]],
        [[1, 2, 3, 4], 5, [4, 1, 2, 3]],
        # [[0, 0, 0], 1, [0, 0, 0]],
        [[3, 5, 1, 1, 2], 1, []],
        # [[-1, -2, -3, -4], 1, [-4, -1, -2, -3]],
    ]
    # list, rotate, answer
    for a, b, c in sample:
        ans = solution(a, b)
        print('Ans :', ans, ' Rotate : ', b, end = '\n\n')
