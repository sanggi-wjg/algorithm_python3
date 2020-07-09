import sys

N, K = map(int, sys.stdin.readline().split())

s = [i + 1 for i in range(N)]

result = []
r = K - 1

while s:
    if len(s) <= r:
        r = r - len(s)
    else:
        result.append(s.pop(r))
        r = r + (K - 1)

print('<', end = '')
for i, r in enumerate(result):
    print('{}, '.format(r), end = '') if i < len(result) - 1 else print(r, end = '')
print('>')
