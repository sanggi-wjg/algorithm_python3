import collections


def solution(N: int, stages: list):
    answer, num_player = dict(), len(stages)
    stages = dict(sorted(collections.Counter(stages).items()))

    for i in range(N):
        if i + 1 in stages.keys():
            answer.setdefault(i + 1, stages.get(i + 1) / num_player)
            num_player -= stages.get(i + 1)
        else:
            answer.setdefault(i + 1, 0)

    # print(stages, answer)
    return [p[0] for p in list(sorted(answer.items(), key = lambda x: x[1], reverse = True))]


if __name__ == '__main__':
    test = [
        [5, [2, 1, 2, 6, 2, 4, 3, 3]],
        [4, [4, 4, 4, 4, 4]],
    ]

    for a, b in test:
        print(solution(a, b))
