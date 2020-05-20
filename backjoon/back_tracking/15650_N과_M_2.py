import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

data = [n + 1 for n in range(N)]
data = permutations(data, M)

# 중복 제거
result = [sorted(d) for d in data]
result = sorted(set(map(tuple, result)))

for r in result:
    sys.stdout.writelines('{}\n'.format(' '.join(map(str, r))))
