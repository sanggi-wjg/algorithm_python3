import sys

N = int(sys.stdin.readline())
X, Y = [], []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

zipped = zip(X, Y)
zipped = sorted(zipped, key = lambda a: (a[0], a[1]))

for x, y in zipped:
    sys.stdout.writelines('{} {}\n'.format(x, y))
