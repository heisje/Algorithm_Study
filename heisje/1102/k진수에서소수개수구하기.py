def to_k_notation(n, k):
    if n == k:
        return '10'
    elif n < k:
        return str(n)
    return to_k_notation(n // k, k) + str(n % k)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    visited = {}
    
    for prime_cand in to_k_notation(n, k).split('0'):
        if prime_cand:
            pc = int(prime_cand)
            try:
                if visited[pc]:
                    answer += 1
            except:
                if is_prime(pc):
                    visited[pc] = 1
                    answer += 1
                else:
                    visited[pc] = 0

    return answer

# 테스트 1 〉	통과 (89.82ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.04ms, 10MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 테스트 11 〉	통과 (0.05ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.03ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)

# LV2