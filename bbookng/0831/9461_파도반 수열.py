import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dp = [0, 1, 1, 1, 2]
    N = int(input())
    for i in range(5, N+1):             # 그냥..규칙..
        dp.append(dp[i-2] + dp[i-3])
    print(dp[N])