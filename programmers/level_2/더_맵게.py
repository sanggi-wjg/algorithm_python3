import heapq


def solution(scoville: list, K: int):
    heap = []
    answer = 0

    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        try:
            min_1 = heapq.heappop(heap)
            min_2 = heapq.heappop(heap)
        except IndexError:
            return -1

        heapq.heappush(heap, min_1 + (min_2 * 2))

        answer += 1

    return answer


if __name__ == '__main__':
    test = [
        [[1, 2, 3, 9, 10, 12], 7],
        [[1, 2, 3, 9, 10, 12], 1000]
    ]

    for a, b in test:
        print(solution(a, b))
