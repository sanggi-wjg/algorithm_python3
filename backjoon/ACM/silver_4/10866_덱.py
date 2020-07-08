import collections
import sys

N = int(sys.stdin.readline())

q = collections.deque()

for n in range(N):
    order = sys.stdin.readline().split()

    if len(order) == 1:
        a = order[0]
        if a == 'front':
            print(q[0]) if q else print(-1)
        elif a == 'back':
            print(q[-1]) if q else print(-1)
        elif a == 'size':
            print(len(q))
        elif a == 'empty':
            print(0) if q else print(1)
        elif a == 'pop_front':
            print(q.popleft()) if len(q) > 0 else print(-1)
        elif a == 'pop_back':
            print(q.pop()) if len(q) > 0 else print(-1)

    else:
        a, b = order[0], order[1]
        if a == 'push_front':
            q.appendleft(b)
        elif a == 'push_back':
            q.append(b)
