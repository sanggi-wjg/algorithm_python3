import sys

N = int(input())
X, Y = [], []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

zipped = zip(X, Y)
zipped = sorted(zipped, key = lambda a: (a[1], a[0]))

for x, y in zipped:
    sys.stdout.writelines('{} {}\n'.format(x, y))
