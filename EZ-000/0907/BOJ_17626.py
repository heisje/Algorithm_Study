from math import trunc


def sqr4(sqrt1):
    if N == sqrt1 ** 2:         # N이 제곱수인 경우 return 1
        return 1

    while True:                 # trunc(sqrt(N)) ~ 0까지 N이 a ** 2 + b ** 2인 경우가 있는지 확인
        if sqrt1 == 0:          # 최대 trunc(sqrt(50000))번
            break
        sqrt2 = trunc((N - sqrt1 ** 2) ** (1 / 2))
        if (N - sqrt1 ** 2) == sqrt2 ** 2:
            return 2
        sqrt1 -= 1

    n = 0                       # 라그랑주의 네 제곱수 정리 중
    while True:                 # (4 ** n)(8 * k + 7) 형태의 수는 3개의 제곱수의 합으로 나타낼 수 X
        if N < 4 ** n:          # 최대 8번 (50000 < 4 ** 8)
            break
        if (N / (4 ** n) - 7) % 8 == 0:
            return 4
        n += 1

    return 3                    # 위의 세 가지 경우가 아니라면 return 3


N = int(input())
sqrt = trunc(N ** (1 / 2))
print(sqr4(sqrt))




''' Dynamic Programming
[출처] https://donghak-dev.tistory.com/49
N = int(input())
dp = [0, 1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j ** 2) <= i:
        min_value = min(min_value, dp[i - (j ** 2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])
'''
