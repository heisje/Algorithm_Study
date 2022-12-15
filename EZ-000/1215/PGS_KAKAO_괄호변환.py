def right(s):
    s = list(s)
    flag = 0
    for c in s:
        flag += 1 if c == '(' else -1
        if flag < 0:
            return False
    return True


def flip(pars):
    result = ''
    for par in pars:
        result += ')' if par == '(' else '('
    return result


def solution(p):
    if right(p):
        return p
    else:
        p = list(p)
        check = 0
        idx = 0
        L = len(p)
        for i in range(L):
            if p[i] == '(':
                check += 1
            else:
                check -= 1
            if check == 0:
                idx = i + 1
                break
        u = ''.join(p[:idx])
        v = ''.join(p[idx:])
        if right(u):
            return u + solution(v)
        else:
            temp = '(' + solution(v) + ')' + flip(u[1:-1])
            return temp

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.02ms, 10.2MB)
# 테스트 11 〉	통과 (0.05ms, 10MB)
# 테스트 12 〉	통과 (0.03ms, 10.1MB)
# 테스트 13 〉	통과 (0.05ms, 10.1MB)
# 테스트 14 〉	통과 (0.13ms, 10.4MB)
# 테스트 15 〉	통과 (0.21ms, 10.3MB)
# 테스트 16 〉	통과 (0.42ms, 10.2MB)
# 테스트 17 〉	통과 (0.52ms, 10.2MB)
# 테스트 18 〉	통과 (0.94ms, 10.2MB)
# 테스트 19 〉	통과 (1.23ms, 10.4MB)
# 테스트 20 〉	통과 (1.97ms, 10.4MB)
# 테스트 21 〉	통과 (0.41ms, 10.2MB)
# 테스트 22 〉	통과 (0.21ms, 10.1MB)
# 테스트 23 〉	통과 (0.71ms, 10.3MB)
# 테스트 24 〉	통과 (0.11ms, 10.2MB)
# 테스트 25 〉	통과 (0.41ms, 10.2MB)
