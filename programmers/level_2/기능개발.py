def solution(progresses: list, speeds: list):
    answer = []
    # task = dict(p for p in enumerate(progresses))
    # print(task)
    count = 0

    while progresses:
        # print(progresses, speeds)

        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if len(progresses) == 0: answer.append(count)
        else:
            if count != 0: answer.append(count)
            count = 0

            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    return answer


test = [
    [[93, 30, 55], [1, 30, 5]],
    [[90, 90, 90], [1, 1, 1]],
    [[93, 30, 55, 60], [1, 30, 5, 40]],
    [[93, 30, 55, 10, 10, 10], [1, 10, 5, 1, 1, 1]],
]

for a, b in test:
    ans = solution(a, b)
    print(ans)
