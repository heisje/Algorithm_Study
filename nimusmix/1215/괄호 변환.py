from collections import deque

def uv_split(bracket):
    op = cl = 0
    for idx, i in enumerate(bracket):
        if i == '(':
            op += 1
        else:
            cl += 1
        
        if op == cl:
            u = bracket[:idx+1]
            v = bracket[idx+1:]
            return u, v


def check(bracket):
    stack = deque()
    
    for i in bracket:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                return False
    
    if stack:
        return False
    
    return True


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
    if not p:
        return ''

    # 2. 문자열을 u, v로 분리한다.
    u, v = uv_split(p)
    
    # 3. 문자열 u가 올바른 괄호 문자열이라면, 문자열 v에 대해 1단계부터 다시 수행한다.
    if check(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환한다.
        return u + solution(v)
    
    # 4. 문자열 u가 올바른 괄호 문자열이 아니라면,
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙인다.
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        # 4-3. ')'를 다시 붙인다.
        ans = '(' + solution(v) + ')'
        
        # 4-4. u의 첫 번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
        u = u[1:-1]
        for i in u:
            if i == '(':
                ans += ')'
            else:
                ans += '('
                
        # 4-5. 생성된 문자열을 반환한다.
        return ans


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.4MB)
# 테스트 13 〉	통과 (0.03ms, 10.3MB)
# 테스트 14 〉	통과 (0.05ms, 10.3MB)
# 테스트 15 〉	통과 (0.09ms, 10.4MB)
# 테스트 16 〉	통과 (0.13ms, 10.3MB)
# 테스트 17 〉	통과 (0.12ms, 10.3MB)
# 테스트 18 〉	통과 (0.17ms, 10.2MB)
# 테스트 19 〉	통과 (0.24ms, 10.3MB)
# 테스트 20 〉	통과 (0.29ms, 10.3MB)
# 테스트 21 〉	통과 (0.19ms, 10.3MB)
# 테스트 22 〉	통과 (0.10ms, 10.2MB)
# 테스트 23 〉	통과 (0.17ms, 10.2MB)
# 테스트 24 〉	통과 (0.08ms, 10.3MB)
# 테스트 25 〉	통과 (0.13ms, 10.2MB)