import sys

N = int(sys.stdin.readline())
IDXS, AGES, NAMES = [], [], []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    IDXS.append(i)
    AGES.append(age)
    NAMES.append(name)

zipped = zip(IDXS, AGES, NAMES)
zipped = sorted(zipped, key = lambda x: (int(x[1]), x[0],))

for idx, age, name in zipped:
    sys.stdout.writelines('{} {}\n'.format(age, name))
