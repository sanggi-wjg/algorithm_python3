import sys

N = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(N)]


def solution(word_list):
    result_string = ''

    for i in range(len(word_list[0])):
        base = word_list[0][i]
        is_diff = False

        for word in word_list:
            if word[i] != base:
                is_diff = True
                break

        if not is_diff:
            result_string += base
        else:
            result_string += '?'

    return result_string


result = solution(word_list)
sys.stdout.writelines(result)
