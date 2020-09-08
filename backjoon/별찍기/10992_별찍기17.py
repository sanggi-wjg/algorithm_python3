N = int(input())

for i in range(N):
    if i == 0:
        print(' ' * (N - 1) + '*')
    elif i == N - 1:
        print(('*' * (N - 1)) + '*' + ('*' * (N - 1)))
    else:
        print((' ' * (N - i - 1)) + '*' + (' ' * i) + (' ' * (i - 1)) + '*')

"""
1
*

2
 *
***

3
  *
 * *
*****

4
   *
  * *
 *   *
*******
"""
