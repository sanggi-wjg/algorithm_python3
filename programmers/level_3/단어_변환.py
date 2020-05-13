def solution(begin: str, target: str, words: list):
    answer = 0

    return answer


test = [
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
]

ANSWER = [
    4, 0
]

for a, b, c in test:
    ans = solution(a, b, c)
    print(ans)
