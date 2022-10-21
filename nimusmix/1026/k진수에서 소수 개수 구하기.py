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


# 에라토스테네스의 체
# def prime_list(x):
#     sieve = [1] * x
#     root = int(x ** 0.5)

#     for i in range(2, root+1):
#         if sieve[i] == True:
#             for j in range(i+i, x, i):
#                 sieve[j] = False
    
#     return [i for i in range(2, x) if sieve[i] == True]