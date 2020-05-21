import collections
import sys

N = int(sys.stdin.readline())
orders = []

for _ in range(N):
    orders.append(sys.stdin.readline().rstrip())

queue = collections.deque()

for order in orders:

    if order.startswith('push'):
        queue.append(order.split(' ')[1])

    elif order.startswith('pop'):
        if len(queue) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(queue.popleft() + '\n')

    elif order.startswith('size'):
        sys.stdout.write(str(len(queue)) + '\n')

    elif order.startswith('empty'):
        sys.stdout.write('1\n') if len(queue) == 0 else sys.stdout.write('0\n')

    elif order.startswith('front'):
        sys.stdout.write(queue[0] + '\n') if len(queue) != 0 else sys.stdout.write('-1\n')

    elif order.startswith('back'):
        sys.stdout.write(queue[-1] + '\n') if len(queue) != 0 else sys.stdout.write('-1\n')
