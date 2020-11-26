# N = int(input())
# if N == 1:
#     print('*')
#     exit()
from pprint import pprint


def _get_seq(n: int, a: int, d: int):
    return a + (n - 1) * d


def _draw_board(n: int):
    row_seq = _get_seq(n, 6, 4)
    col_seq = _get_seq(n, 5, 4)

    return [['*' * col_seq] * row_seq]


def solution(n: int):
    board = _draw_board(n)
    board_len = len(board)
    pprint(board)

    for i in range(board_len):
        for


n = 2
solution(n - 1)
# print('\n------------\n')

"""
6 10 14 
an = a + (n-1)d
a1 = a = 6
a2 = 6 + (1)4 = 10  
a3 = 6 + (2)4 = 14

5 9 13
a1 = a = 5
a2 = 5 + (1)4 = 9
a3 = 5 + (2)4 = 13

2 (row 7) (col 5)
*****
*
* ***
* * *
* * *
*   *
*****

3 (10) (9)
*********
*
* *******
* *     *
* * *** *
* * * * *
* * * * *
* *   * *
* ***** *
*       *
*********

4 (14) (13)
*************
*
* ***********
* *         *
* * ******* *
* * *     * *
* * * *** * *
* * * * * * *
* * * * * * *
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************
"""
