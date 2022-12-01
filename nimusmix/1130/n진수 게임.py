def solution(n, t, m, p):
    answer = '0'
    
    def notation(num):
        tmp = ''
        over_ten = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        
        while num > 0:
            num, r = divmod(num, n)
            
            if r in over_ten.keys():
                tmp += over_ten[r]
            else:
                tmp += str(r)
        return tmp[::-1]

    
    for i in range(1, t*m):
        answer += notation(i)
            
    check = ''
    for i in range(p-1, t*m, m):
        check += str(answer[i])

    return check


# 테스트 1 〉	통과 (0.03ms, 10MB)
# 테스트 2 〉	통과 (0.06ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.1MB)
# 테스트 4 〉	통과 (0.07ms, 10.3MB)
# 테스트 5 〉	통과 (1.22ms, 10.2MB)
# 테스트 6 〉	통과 (2.28ms, 10.2MB)
# 테스트 7 〉	통과 (1.31ms, 10.3MB)
# 테스트 8 〉	통과 (0.53ms, 10.1MB)
# 테스트 9 〉	통과 (0.94ms, 10.2MB)
# 테스트 10 〉	통과 (0.54ms, 10.1MB)
# 테스트 11 〉	통과 (0.45ms, 10.1MB)
# 테스트 12 〉	통과 (0.46ms, 10.2MB)
# 테스트 13 〉	통과 (0.49ms, 10.2MB)
# 테스트 14 〉	통과 (151.72ms, 10.4MB)
# 테스트 15 〉	통과 (154.48ms, 10.5MB)
# 테스트 16 〉	통과 (148.04ms, 10.3MB)
# 테스트 17 〉	통과 (9.87ms, 10.2MB)
# 테스트 18 〉	통과 (5.80ms, 9.94MB)
# 테스트 19 〉	통과 (2.12ms, 10.1MB)
# 테스트 20 〉	통과 (4.62ms, 10.1MB)
# 테스트 21 〉	통과 (34.15ms, 10.2MB)
# 테스트 22 〉	통과 (21.78ms, 9.98MB)
# 테스트 23 〉	통과 (77.19ms, 10.4MB)
# 테스트 24 〉	통과 (173.74ms, 10.4MB)
# 테스트 25 〉	통과 (230.45ms, 10.6MB)
# 테스트 26 〉	통과 (19.76ms, 10.2MB)