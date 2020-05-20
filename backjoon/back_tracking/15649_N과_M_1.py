import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

result = [n + 1 for n in range(N)]
result = permutations(result, M)
result = sorted(list(set(result)))

for r in result:
    sys.stdout.writelines('{}\n'.format(' '.join(map(str, list(r)))))
