def calculator(ex):
    stack = []
    for term in ex:
        if term not in ('*', '+', '-'):
            stack.append(term)
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            if term == '*':
                stack.append(t1 * t2)
            elif term == '+':
                stack.append(t1 + t2)
            elif term == '-':
                stack.append(t1 - t2)
    return stack[0]


priorities = [
    {'*': 3, '+': 2, '-': 1},
    {'*': 3, '+': 1, '-': 2},
    {'*': 2, '+': 3, '-': 1},
    {'*': 2, '+': 1, '-': 3},
    {'*': 1, '+': 3, '-': 2},
    {'*': 1, '+': 2, '-': 3}
]


def solution(expression):
    infix = []
    temp = ''
    for c in expression:
        if c not in ('*', '+', '-'):
            temp += c
        else:
            infix.append(temp)
            infix.append(c)
            temp = ''
    infix.append(temp)

    postfix = []
    operators = []  # stack
    max_prize = 0
    for priority in priorities:
        for c in infix:
            if c not in ('*', '+', '-'):
                postfix.append(int(c))
            else:
                while True:
                    if not operators or priority[operators[-1]] < priority[c]:
                        operators.append(c)
                        break
                    else:
                        postfix.append(operators.pop())
        if operators:
            postfix.extend(operators[::-1])
            operators = []
        temp = abs(calculator(postfix))
        if max_prize < temp:
            max_prize = temp
        postfix = []

    return max_prize

# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.12ms, 10.4MB)
# 테스트 4 〉	통과 (0.12ms, 10.4MB)
# 테스트 5 〉	통과 (0.09ms, 10.3MB)
# 테스트 6 〉	통과 (0.14ms, 10.4MB)
# 테스트 7 〉	통과 (0.15ms, 10.4MB)
# 테스트 8 〉	통과 (0.18ms, 10.5MB)
# 테스트 9 〉	통과 (0.11ms, 10.4MB)
# 테스트 10 〉	통과 (0.12ms, 10.5MB)
# 테스트 11 〉	통과 (0.11ms, 10.3MB)
# 테스트 12 〉	통과 (0.24ms, 10.3MB)
# 테스트 13 〉	통과 (0.13ms, 10.4MB)
# 테스트 14 〉	통과 (0.28ms, 10.4MB)
# 테스트 15 〉	통과 (0.32ms, 10.4MB)
# 테스트 16 〉	통과 (0.06ms, 10.4MB)
# 테스트 17 〉	통과 (0.06ms, 10.3MB)
# 테스트 18 〉	통과 (0.06ms, 10.4MB)
# 테스트 19 〉	통과 (0.08ms, 10.3MB)
# 테스트 20 〉	통과 (0.05ms, 10.3MB)
# 테스트 21 〉	통과 (0.16ms, 10.3MB)
# 테스트 22 〉	통과 (0.18ms, 10.4MB)
# 테스트 23 〉	통과 (0.04ms, 10.4MB)
# 테스트 24 〉	통과 (0.17ms, 10.4MB)
# 테스트 25 〉	통과 (0.16ms, 10.3MB)
# 테스트 26 〉	통과 (0.04ms, 10.3MB)
# 테스트 27 〉	통과 (0.17ms, 10.3MB)
# 테스트 28 〉	통과 (0.18ms, 10.3MB)
# 테스트 29 〉	통과 (0.15ms, 10.4MB)
# 테스트 30 〉	통과 (0.28ms, 10.3MB)
