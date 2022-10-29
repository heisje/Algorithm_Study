def is_prime(x):
    root = int(x ** 0.5)
    for i in range(2, root+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    digit = []
    share, rest = n, k

    while share >= k:
        share, rest = share // k, share % k
        digit.append(str(rest))

    digit.append(str(share % k))
    digit.reverse()
    digit = ''.join(digit)

    d_list = digit.split('0')

    answer = 0
    for i in d_list:
        if i and i != '1' and is_prime(int(i)):
            answer += 1

    return answer


# 테스트 1 〉	통과 (100.18ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.4MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.4MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.4MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)