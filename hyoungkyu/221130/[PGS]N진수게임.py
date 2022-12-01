def jinsu(num, n):
    hihi = []
    while True:                     # 진수 변환 코드
        if num // n == 0:
            if num >= 10:
                num = chr(55+num)   # 아스키 코드 변환
            hihi.append(num)
            break
        tmp = num%n
        if tmp >= 10:
            tmp = chr(55+tmp)       # 아스키 코드 변환
        hihi.append(tmp)
        num = num // n
    hihi.reverse()                  # 변환한 값 뒤집기
    return "".join(map(str,hihi))   # 문자열로 변환

def solution(n, t, m, p):           # n : 진법, t : 미리 구할 숫자의 개수, m : 참가 인원, p : 튜브의 순서
    answer = ''
    s = ''
    num = -1
    while len(s) <= t*m:            # 숫자를 증가시키면서 문자열 더하기
        num += 1
        s += jinsu(num, n)
    for i in range(p-1, len(s), m):
        answer += s[i]
        if len(answer) == t:
            break
        
    return answer

'''
테스트 1 〉통과 (0.01ms, 10.2MB)
테스트 2 〉통과 (0.03ms, 10.2MB)
테스트 3 〉통과 (0.03ms, 10.2MB)
테스트 4 〉통과 (0.04ms, 10.4MB)
테스트 5 〉통과 (0.16ms, 10.2MB)
테스트 6 〉통과 (0.16ms, 10.4MB)
테스트 7 〉통과 (0.16ms, 10.2MB)
테스트 8 〉통과 (0.21ms, 10.2MB)
테스트 9 〉통과 (0.19ms, 10.3MB)
테스트 10 〉통과 (0.19ms, 10.3MB)
테스트 11 〉통과 (0.22ms, 10.2MB)
테스트 12 〉통과 (0.21ms, 10.2MB)
테스트 13 〉통과 (0.40ms, 10.4MB)
테스트 14 〉통과 (37.11ms, 10.4MB)
테스트 15 〉통과 (36.94ms, 10.4MB)
테스트 16 〉통과 (36.92ms, 10.3MB)
테스트 17 〉통과 (1.32ms, 10.2MB)
테스트 18 〉통과 (2.08ms, 10.4MB)
테스트 19 〉통과 (0.78ms, 10.2MB)
테스트 20 〉통과 (1.89ms, 10.2MB)
테스트 21 〉통과 (9.22ms, 10.3MB)
테스트 22 〉통과 (5.49ms, 10.4MB)
테스트 23 〉통과 (12.67ms, 10.3MB)
테스트 24 〉통과 (16.28ms, 10.5MB)
테스트 25 〉통과 (19.31ms, 10.4MB)
테스트 26 〉통과 (5.92ms, 10.4MB)
'''