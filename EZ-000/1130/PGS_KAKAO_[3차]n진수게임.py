def base(num, q):
    rev_base = ''
    while num > 0:
        num, mod = divmod(num, q)
        if 9 < mod:
            rev_base += chr(mod + 55)
        else:
            rev_base += str(mod)

    return rev_base[::-1]
# 참고: https://velog.io/@code_angler/파이썬-진수변환2진법-3진법-5진법-10진법n진법


def solution(n, t, m, p):
    answer = ''
    total = '0'
    cnt = 1
    while len(total) < t * m:
        temp = base(cnt, n)
        total += temp
        cnt += 1
    for i in range(t):
        answer += total[m * i + (p - 1)]

    return answer


# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10MB)
# 테스트 4 〉	통과 (0.05ms, 10.1MB)
# 테스트 5 〉	통과 (0.14ms, 10.3MB)
# 테스트 6 〉	통과 (0.14ms, 10.4MB)
# 테스트 7 〉	통과 (0.15ms, 10.2MB)
# 테스트 8 〉	통과 (0.32ms, 10.3MB)
# 테스트 9 〉	통과 (0.32ms, 10.3MB)
# 테스트 10 〉 통과 (0.27ms, 10.3MB)
# 테스트 11 〉 통과 (0.17ms, 10.1MB)
# 테스트 12 〉 통과 (0.17ms, 10.2MB)
# 테스트 13 〉 통과 (0.19ms, 10.2MB)
# 테스트 14 〉 통과 (31.54ms, 10.3MB)
# 테스트 15 〉 통과 (30.93ms, 10.2MB)
# 테스트 16 〉 통과 (31.43ms, 10.4MB)
# 테스트 17 〉 통과 (2.58ms, 10.2MB)
# 테스트 18 〉 통과 (1.93ms, 10.1MB)
# 테스트 19 〉 통과 (0.47ms, 10.3MB)
# 테스트 20 〉 통과 (1.49ms, 10.2MB)
# 테스트 21 〉 통과 (8.58ms, 10.1MB)
# 테스트 22 〉 통과 (3.50ms, 10.3MB)
# 테스트 23 〉 통과 (21.33ms, 10.2MB)
# 테스트 24 〉 통과 (28.35ms, 10.3MB)
# 테스트 25 〉 통과 (12.59ms, 10.2MB)
# 테스트 26 〉 통과 (4.41ms, 10.2MB)
