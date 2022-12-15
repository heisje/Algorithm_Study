def solution(p):
    answer = ''
    if len(p) == 0:
        return answer
    else:
        normal = True
        open_count = 0
        close_count = 0
        cut_point = 0
        for i in range(len(p)):
            if p[i] == '(':
                open_count += 1
            else:
                close_count += 1

            if open_count - close_count < 0:
                normal = False

            if open_count == close_count:
                cut_point = i + 1
                break
        returned_p = solution(p[cut_point:])
        if normal:
            return p[:cut_point] + returned_p
        else:
            temp = ''
            for j in range(1, cut_point - 1):
                if p[j] == '(':
                    temp = temp + ')'
                else:
                    temp = temp + '('
            return '(' + returned_p + ')' + temp



print(solution("()))((()"))

"""
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.3MB)
테스트 16 〉	통과 (0.13ms, 10.4MB)
테스트 17 〉	통과 (0.10ms, 10.3MB)
테스트 18 〉	통과 (0.15ms, 10.3MB)
테스트 19 〉	통과 (0.47ms, 10.3MB)
테스트 20 〉	통과 (0.20ms, 10.2MB)
테스트 21 〉	통과 (0.23ms, 10.2MB)
테스트 22 〉	통과 (0.11ms, 10.3MB)
테스트 23 〉	통과 (0.30ms, 10.2MB)
테스트 24 〉	통과 (0.07ms, 10.2MB)
테스트 25 〉	통과 (0.10ms, 10.2MB)
"""