N = int(input())


def get_seq(n, a = 1, d = 4):
    return a + (n - 1) * d


def solution(n):
    seq = get_seq(n)
    recur = { 'prev': 1, 'next': 0 }
    flag = False

    for i in range(seq):
        if i == 0 or i == seq - 1:
            print('*' * seq)

        elif i % 2 != 0:
            print('* ' * recur['prev'] + ' ' * get_seq(n - recur['prev']) + ' *' * recur['prev'])

            if not flag:
                recur['prev'] += 1
                recur['next'] += 1

        elif i % 2 == 0:
            print('* ' * recur['next'] + '*' * get_seq(n - recur['next']) + ' *' * recur['next'])

            if get_seq(n - recur['next']) == 1:
                flag = True

            if flag:
                recur['prev'] -= 1
                recur['next'] -= 1


solution(N)

# solution(2)
# print('\n------------\n')
# solution(3)
# print('\n------------\n')
# solution(4)

"""
5 9 13
공차 4
an = a + (n-1)d
a1 = a = 1
a2 = a + 4 = 1 + 4 = 5
a3 = a + 8 = 1 + 8 = 9 
a4 = a + 12 = 1 + 9 = 13

3 5 7 
a1 = 3
a2 = 3 + 2 = 5
a3 = 3 + 4 = 7
"""
"""
2 (5)
*****  5
*   *  space 3
* * *
*   *
*****

3 (9)
*********  9
*       *  space 7
* ***** *  7
* *   * *
* * * * *
* *   * *
* ***** *
*       *
*********

4 (13)
*************  13
*           *  space 11
* ********* *  11
* *       * *
* * ***** * *
* * *   * * *
* * * * * * *
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************
"""
