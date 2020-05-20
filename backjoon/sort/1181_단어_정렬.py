import sys

N = int(sys.stdin.readline())
words = []

for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

words = sorted(list(set(words)))
words = sorted(words, key = len)

for w in words:
    sys.stdout.writelines('{}\n'.format(w))
