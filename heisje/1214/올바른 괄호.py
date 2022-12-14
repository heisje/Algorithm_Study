# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 10분
def solution(s):
    answer = True
    
    stack = []
    for ss in s:
        if ss == "(":
            stack.append(1)
        if ss == ")":
            if stack and stack[-1] == 1:
                stack.pop()
            else:
                return False
    else:
        if stack == []:
            return True
    return False


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))


# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.00ms, 10.1MB)
# 테스트 7 〉	통과 (0.00ms, 10.3MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.02ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 효율성  테스트
# 테스트 1 〉	통과 (9.61ms, 10.4MB)
# 테스트 2 〉	통과 (8.78ms, 10.3MB)