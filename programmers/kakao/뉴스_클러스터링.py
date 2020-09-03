import collections
import re


def count_set(txt1: list, txt2: list) -> int:
    txt1 = collections.Counter(txt1)
    txt2 = collections.Counter(txt2)

    equal_list = txt1 & txt2
    total_list = (txt1 | txt2)

    count_equal = sum(equal_list.values())
    count_total = sum(total_list.values())

    # if count_equal == 0:
    #     return 65536

    return int((count_equal / count_total) * 65536)


def remove_invalid(txt: list) -> list:
    invalid_index = []
    for i in range(len(txt)):
        t = re.findall('[A-Z]', txt[i])
        if len(t) != 2:
            invalid_index.append(i)

    if invalid_index:
        invalid_index.reverse()
        for index in invalid_index:
            txt.pop(index)

    return txt


def solution(str1: str, str2: str) -> int:
    s1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1)]
    s2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1)]

    s1 = remove_invalid(s1)
    s2 = remove_invalid(s2)

    if not s1 and not s2:
        return 65536

    return count_set(s1, s2)


sample = [
    ["FRANCE", 'french', 16384],
    ["handshake", 'shake hands', 65536],
    ["aa1+aa2", "AAAA12", 43690],
    ['E=M*C^2', 'e=m*c^2', 65536],
    ['aa', 'zz', 65536],
    # ['aab', 'aazaab', 65536],
]

for a, b, c in sample:
    r = solution(a, b)
    print('Equal /' if r == c else 'Not Equal /', r, '/', c, '\n')
