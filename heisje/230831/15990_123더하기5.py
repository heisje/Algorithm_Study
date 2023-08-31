import sys
input = sys.stdin.readline

dp = [[],[],[]]
dp[0], dp[1], dp[2] = [1, 0 ,0], [0, 1, 0], [1, 1, 1]

Q = []
for _ in range(int(input())):
    Q.append(int(input()))

answer = []
for i in range(3, max(Q)):
    dp.append([0,0,0])
    dp[i][2] += (dp[i-3][0] + dp[i-3][1]) % 1000000009
    dp[i][1] += (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][0] += (dp[i-1][1] + dp[i-1][2]) % 1000000009

for q in Q:
    print(sum(dp[q-1]) % 1000000009)