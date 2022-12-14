# https://school.programmers.co.kr/learn/courses/30/lessons/60058
# 문제 개싫어


def solution(p):
    p = list(p)
    u = []
    v = []

    left = 0
    right = 0

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == []:
        return ""
    idx = -1

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    while idx < len(p):
        idx += 1
        if p[idx] == "(":
            left += 1
        if p[idx] == ")":
            right += 1

        if left > 0 and left == right:
            u = p[:idx+1]
            v = p[idx+1:]
            break

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    stack = []
    for idx, value in enumerate(u) :
        if value == "(":
            stack.append("(")
        if value == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")()()()()(()()(((())))()()()()()(")
                break

    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    if not stack:
        return "".join(u) + solution("".join(v))

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    if stack:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        temp = "("

        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        temp += solution("".join(v))

        # 4-3. ')'를 다시 붙입니다. 
        temp += ")" 

        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        u.pop()
        u.pop(0)
        for idx in range(len(u)):
            if u[idx] == "(":
                u[idx] = ")"
            elif u[idx] == ")":
                u[idx] = "("
        temp += "".join(u)
        # 4-5. 생성된 문자열을 반환합니다.
        return temp


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.1MB)
# 테스트 13 〉	통과 (0.06ms, 10.2MB)
# 테스트 14 〉	통과 (0.13ms, 10.3MB)
# 테스트 15 〉	통과 (0.18ms, 10.3MB)
# 테스트 16 〉	통과 (0.48ms, 10.3MB)
# 테스트 17 〉	통과 (0.59ms, 10.3MB)
# 테스트 18 〉	통과 (0.70ms, 10.5MB)
# 테스트 19 〉	통과 (1.31ms, 10.8MB)
# 테스트 20 〉	통과 (1.14ms, 10.4MB)
# 테스트 21 〉	통과 (0.47ms, 10.1MB)
# 테스트 22 〉	통과 (0.26ms, 10.4MB)
# 테스트 23 〉	통과 (0.77ms, 10.5MB)
# 테스트 24 〉	통과 (0.40ms, 10.1MB)
# 테스트 25 〉	통과 (0.66ms, 10.4MB)