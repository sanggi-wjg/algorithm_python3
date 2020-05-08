import heapq


def solution(rest: int, dates: list, supplies: list, K: int):
    answer, idx, heap = 0, 0, []

    while rest < K:

        for i in range(idx, len(dates)):
            # print(heap)
            if rest < dates[i]:
                break

            heapq.heappush(heap, -supplies[i])
            idx = i + 1

        rest += heapq.heappop(heap) * -1
        answer += 1

    return answer


test = [
    [4, [4, 10, 15], [20, 5, 10], 30],
    [4, [4, 10, 15, 20], [20, 5, 10, 5], 30],
]

for a, b, c, d in test:
    ans = solution(a, b, c, d)
    print(ans)
