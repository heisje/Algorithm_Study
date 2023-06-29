import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

# dp
dp = [0 for _ in range(N)]
dp[0] = 1
std = 0

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            std = max(std, dp[j])

    dp[i] = std + 1
    std = 0

print(N - max(dp))

# queue





