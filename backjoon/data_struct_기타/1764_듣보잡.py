import sys

N, M = map(int, sys.stdin.readline().strip().split())
data = set()
data2 = set()

for _ in range(N):
    data.add(input())

for _ in range(M):
    data2.add(input())

intersection = data.intersection(data2)
intersection = sorted(intersection)
print(len(intersection))
print('\n'.join(intersection))

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

2
baesangwook
ohhenrie
"""
