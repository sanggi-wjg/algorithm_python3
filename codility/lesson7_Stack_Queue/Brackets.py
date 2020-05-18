def solution(S):
    if len(S) == 0:
        return 0

    S = list(map(str, S))
    stack = []

    for s in S:
        if s in ['{', '[', '(']:
            stack.append(s)

        elif s == '}':
            if len(stack) and stack[-1] == '{':
                stack.pop()
            else:
                return 0

        elif s == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                return 0

        elif s == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        # print(stack)

    if len(stack):
        return 0

    return 1


samples = [
    # '',
    # '(',
    # '(}',
    '[](}',
    '[]()',
    '()',
    # '{[()()]}',
    # '}{[()()]}',
    # '([)()]',
    # '([)()]',
]

for sample in samples:
    print('Solution:', solution(sample))
