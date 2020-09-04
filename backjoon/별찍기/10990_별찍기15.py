N = int(input())

for i in range(N, 0, - 1):
    if i == N:
        print((' ' * (i - 1)) + '*')
    else:
        print((' ' * (i - 1)) + '*' + (' ' * ((N - i) * 2 - 1)) + '*')

"""
1
*

2
 *
* *

3
  *
 * *
*   *

4
   *
  * *
 *   *
*     *
"""
