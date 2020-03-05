def solution(strings, n):
    # return sorted(strings, key = lambda x: (x[n:len(x)], x[0:len(x)]))
    return sorted(sorted(strings), key = lambda x: x[n])


test = [
    [["sun", "bed", "car"], 1],
    [["abce", "abcd", "cdx"], 2],
    [['abzcd', 'cdzab', 'abzfg', 'abzaa', 'abzbb', 'bbzaa'], 2]
]

for a, d in test:
    print(solution(a, d))
