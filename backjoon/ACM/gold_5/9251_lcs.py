from pprint import pprint

"""
ACAYKP
CAPCAK

ACAK 4

[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 2, 2, 2],
 [0, 1, 2, 2, 2, 3, 3],
 [0, 1, 2, 2, 2, 3, 3],
 [0, 1, 2, 2, 2, 3, 4],
 [0, 1, 2, 3, 3, 3, 4]]

"""
txt1, txt2 = [input() for _ in range(2)]

length1 = len(txt1)
length2 = len(txt2)
lcs = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        t1 = txt1[i - 1]
        t2 = txt2[j - 1]
        if t1 == t2:
            lcs[i][j] += lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

pprint(lcs)
print(lcs[length1][length2])
