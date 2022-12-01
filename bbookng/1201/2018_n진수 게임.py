def solution(n, t, m, p):
    answer = ''
    numbers = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    result = '0'
    number = 0

    while len(result) <= t * m + p - 1:
        tmp = number
        tmp2 = ''
        while tmp > 0:
            tmp2 = str(numbers[tmp % n]) + tmp2
            tmp //= n
        result += tmp2
        number += 1

    for i in range(p-1, t*m, m):
        answer += result[i]

    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.12ms, 10.1MB)
테스트 6 〉	통과 (0.23ms, 10.2MB)
테스트 7 〉	통과 (0.15ms, 10.1MB)
테스트 8 〉	통과 (0.25ms, 10.3MB)
테스트 9 〉	통과 (0.14ms, 10.1MB)
테스트 10 〉	통과 (0.14ms, 10.2MB)
테스트 11 〉	통과 (0.27ms, 10.1MB)
테스트 12 〉	통과 (0.14ms, 10.1MB)
테스트 13 〉	통과 (0.15ms, 10.3MB)
테스트 14 〉	통과 (30.04ms, 10.3MB)
테스트 15 〉	통과 (33.56ms, 10.5MB)
테스트 16 〉	통과 (36.13ms, 10.4MB)
테스트 17 〉	통과 (1.16ms, 10.2MB)
테스트 18 〉	통과 (2.47ms, 10.2MB)
테스트 19 〉	통과 (0.39ms, 10.4MB)
테스트 20 〉	통과 (1.18ms, 10.2MB)
테스트 21 〉	통과 (11.50ms, 10.4MB)
테스트 22 〉	통과 (5.87ms, 10.1MB)
테스트 23 〉	통과 (16.65ms, 10.3MB)
테스트 24 〉	통과 (26.61ms, 10.4MB)
테스트 25 〉	통과 (19.85ms, 10.3MB)
테스트 26 〉	통과 (4.33ms, 10.2MB)
'''