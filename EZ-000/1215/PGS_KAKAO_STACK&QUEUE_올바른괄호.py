def solution(s):
    s = list(s)
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    answer = False if stack else True
    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.00ms, 10MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 9.98MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10MB)
테스트 15 〉	통과 (0.03ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 9.98MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)

효율성  테스트
테스트 1 〉	통과 (8.89ms, 11.1MB)
테스트 2 〉	통과 (8.16ms, 11.2MB)
"""
