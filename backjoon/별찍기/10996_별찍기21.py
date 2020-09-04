N = int(input())

if N == 1:
    print('*')
    exit()

for i in range(N):
    if N % 2 == 0:
        print(('* ' * (N // 2)).strip())
    else:
        print(('* ' * ((N + 1) // 2)).strip())
    print(' *' * (N // 2))

"""
1
*

2
*
 *
*
 *

3
* *
 *
* *
 *
* *
 *

4
* *
 * *
* *
 * *
* *
 * *
* *
 * *
"""
