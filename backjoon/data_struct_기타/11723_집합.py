import sys

M = int(sys.stdin.readline())
data = set()

for _ in range(M):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == 'all':
            data = set([n for n in range(1, 21)])
        else:  # empty
            data = set()

    else:
        command, number = order[0], int(order[1])

        if command == 'add':
            data.add(number)

        elif command == 'remove':
            data.discard(number)

        elif command == 'check':
            if number in data:
                sys.stdout.writelines('1\n')
            else:
                sys.stdout.writelines('0\n')

        else:  # toggle
            if number in data:
                data.discard(number)
            else:
                data.add(number)

"""
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
"""
