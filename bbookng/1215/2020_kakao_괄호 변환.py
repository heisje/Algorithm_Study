def division(x):
    left, right = 0, 0

    for i in range(len(x)):
        if x[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = x[:i+1]
            v = x[i+1:]
            return u, v

def check(x):
    tmp = []
    for i in x:
        if i == '(':
            tmp.append(i)
        else:
            if not tmp:
                return False
            tmp.pop()

    if tmp:
        return False
    else:
        return True

def solution(p):
    if not p:
        return p

    answer = ''
    u, v = division(p)

    if check(u):
        return u + solution(v)

    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer

print(solution("(()())()"))

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.23ms, 10.3MB)
테스트 17 〉	통과 (0.13ms, 10.4MB)
테스트 18 〉	통과 (0.19ms, 10.2MB)
테스트 19 〉	통과 (0.40ms, 10.2MB)
테스트 20 〉	통과 (0.37ms, 10.1MB)
테스트 21 〉	통과 (0.40ms, 10.4MB)
테스트 22 〉	통과 (0.18ms, 10.2MB)
테스트 23 〉	통과 (0.20ms, 10.2MB)
테스트 24 〉	통과 (0.11ms, 10.1MB)
테스트 25 〉	통과 (0.28ms, 10.2MB)
'''