n = int(input())
dp = [50001 for _ in range(n+1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        val = j**2
        if val > i: break
        dp[i] = min(dp[i], dp[i-val] + 1)

print(dp[n])