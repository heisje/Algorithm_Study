def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        word_zip = ''
        cnt = 1
        prev = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == prev:
                cnt += 1
            else:
                word_zip += prev if cnt == 1 else str(cnt) + prev
                cnt = 1
                prev = s[j:j+i]
        word_zip += prev if cnt == 1 else str(cnt) + prev
        answer = min(answer, len(word_zip))
    return answer


# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.39ms, 10.1MB)
# 테스트 3 〉	통과 (0.25ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.07ms, 10.1MB)
# 테스트 7 〉	통과 (0.44ms, 10.2MB)
# 테스트 8 〉	통과 (0.44ms, 10.2MB)
# 테스트 9 〉	통과 (0.67ms, 10.3MB)
# 테스트 10 〉	통과 (2.52ms, 10.3MB)
# 테스트 11 〉	통과 (0.17ms, 10.1MB)
# 테스트 12 〉	통과 (0.10ms, 10.1MB)
# 테스트 13 〉	통과 (0.22ms, 10.2MB)
# 테스트 14 〉	통과 (0.66ms, 9.93MB)
# 테스트 15 〉	통과 (0.13ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)
# 테스트 17 〉	통과 (1.45ms, 10.4MB)
# 테스트 18 〉	통과 (1.41ms, 9.98MB)
# 테스트 19 〉	통과 (2.26ms, 10.1MB)
# 테스트 20 〉	통과 (4.48ms, 10MB)
# 테스트 21 〉	통과 (3.04ms, 10.3MB)
# 테스트 22 〉	통과 (2.83ms, 10MB)
# 테스트 23 〉	통과 (2.80ms, 10.1MB)
# 테스트 24 〉	통과 (2.47ms, 10.2MB)
# 테스트 25 〉	통과 (2.74ms, 10.1MB)
# 테스트 26 〉	통과 (2.69ms, 10.2MB)
# 테스트 27 〉	통과 (2.78ms, 10.4MB)
# 테스트 28 〉	통과 (0.02ms, 10.4MB)