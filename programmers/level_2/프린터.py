def solution(task: list, location: int):
    answer = 1
    task = [p for p in enumerate(task)]
    print(task)

    while True:
        cmp = task.pop(0)
        if not task: break

        if max(task, key = lambda x: x[1])[1] > cmp[1]:
            task.append(cmp)

        else:
            if location == cmp[0]:
                break
            answer += 1
        # print(task, ' answer : ', answer)

    return answer


test = [
    [[2, 1, 3, 2], 2, ],
    [[2, 1, 3, 2, 10], 2, ],
    [[1, 1, 9, 1, 1, 1], 0],
    [[3, 3, 4, 2], 3]
]

for a, b in test:
    ans = solution(a, b)
    print(ans)
