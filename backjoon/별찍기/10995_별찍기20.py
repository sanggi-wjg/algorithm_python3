N = int(input())

if N == 1:
    print('*')
    exit()

for i in range(N):
    if i % 2 == 0:
        print('*' + ' *' * (N - 1))
    else:
        print(' *' + ' *' * (N - 1))
"""
1
*

2
* *
 * *

3
* * *
 * * *
* * *

4
* * * *
 * * * *
* * * *
 * * * *
"""
