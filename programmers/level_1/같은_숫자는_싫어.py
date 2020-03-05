def solution(arr):
    answer = [arr[0]]

    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer


test = [
    [1, 1, 3, 3, 0, 1, 1],
    [4, 4, 4, 3, 3]
]

for t in test:
    print(solution(t))
