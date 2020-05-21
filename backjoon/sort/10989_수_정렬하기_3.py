import sys

LIMIT = 10001
N = int(sys.stdin.readline())
data = [0 for i in range(LIMIT)]

for i in range(N):
    data[int(sys.stdin.readline())] += 1

for i in range(1, LIMIT):
    if data[i] > 0:
        sys.stdout.writelines('{}\n'.format(i) * data[i])
