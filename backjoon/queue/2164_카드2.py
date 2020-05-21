import collections
import sys

N = int(sys.stdin.readline())
queue = collections.deque([i for i in range(1, N + 1)])

# print(queue, len(queue))
while len(queue) > 1:
    queue.popleft()
    n = queue.popleft()
    queue.append(n)

# print(queue, len(queue))
print(queue.pop())
