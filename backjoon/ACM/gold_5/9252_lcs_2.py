from pprint import pprint

"""
ACAYKP
CAPCAK

ACAK 4

         C  A  P  C  A  K
     [0, 0, 0, 0, 0, 0, 0],
  A  [0, 0, 1, 1, 1, 1, 1],
  C  [0, 1, 1, 1, 2, 2, 2],
  A  [0, 1, 2, 2, 2, 3, 3],
  Y  [0, 1, 2, 2, 2, 3, 3],
  K  [0, 1, 2, 2, 2, 3, 4],
  P  [0, 1, 2, 3, 3, 3, 4]


XMJYAUZ
MZJAWXU
         M  Z  J  A  W  X  U
     [0, 0, 0, 0, 0, 0, 0, 0],
  X  [0, 0, 0, 0, 0, 0, 1, 1],
  M  [0, 1, 1, 1, 1, 1, 1, 1],
  J  [0, 1, 1, 2, 2, 2, 2, 2],
  Y  [0, 1, 1, 2, 2, 2, 2, 2],
  A  [0, 1, 1, 2, 3, 3, 3, 3],
  U  [0, 1, 1, 2, 3, 3, 3, 4],
  Z  [0, 1, 2, 2, 3, 3, 3, 4]

4
MJAU
"""
txt1, txt2 = [input() for _ in range(2)]

length1 = len(txt1)
length2 = len(txt2)
lcs = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if txt1[i - 1] == txt2[j - 1]:
            lcs[i][j] += lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

lcs_word = ''
x, y = length1, length2

while True:
    if x <= 0 or y <= 0:
        break
    number = lcs[x][y]

    if number > lcs[x][y - 1] and number > lcs[x - 1][y]:
        lcs_word += txt2[y - 1]
        x = x - 1
    else:
        if number == lcs[x][y - 1]:
            y = y - 1
        elif number == lcs[x - 1][y]:
            x = x - 1
        else:
            x = x - 1
            y = y - 1

print(lcs[length1][length2])
print(lcs_word[::-1])
