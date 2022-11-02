def check(num):
    for i in range(2, int(num ** (1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    new = ''

    while n > 0:
        new = str(n % k) + new
        n //= k

    new = new.split('0')

    for i in new:
        if i and i != '1' and check(int(i)):
            answer += 1

    return answer

'''
테스트 1 〉	통과 (90.25ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.5MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.5MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.5MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.02ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.5MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
'''