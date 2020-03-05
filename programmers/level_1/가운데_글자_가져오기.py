def solution(s):
    cnt = len(s)
    return s[int(cnt / 2) - 1:int(cnt / 2) + 1] if cnt % 2 == 0 else s[int(cnt / 2)]


test = [
    'abcde', 'qwer', 'qw',
    'abcdef', 'abcdefg'
]

for t in test:
    print(solution(t))
