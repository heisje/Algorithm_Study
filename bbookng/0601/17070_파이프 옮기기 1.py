from pprint import pprint

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = [1, 0, 0]
dp[0][1] = [1, 0, 0]

# 방향 고려
# 벽 고려
for i in range(N):
    for j in range(1, N):
        if board[i][j]:
            dp[i][j] = [0, 0, 0]
            continue

        # 가로
        if dp[i][j][0] and j < N-1 and not board[i][j+1]:
            dp[i][j+1][0] += dp[i][j][0]
            dp[i + 1][j + 1][2] += dp[i][j][0]

        # 세로
        if dp[i][j][1] and i < N-1 and not board[i+1][j]:
            dp[i+1][j][1] += dp[i][j][1]
            dp[i + 1][j + 1][2] += dp[i][j][1]

        # 대각선
        if dp[i][j][2]:
            if j < N-1 and not board[i][j+1]:
                dp[i][j + 1][0] += dp[i][j][2]
            if i < N-1 and not board[i+1][j]:
                dp[i + 1][j][1] += dp[i][j][2]
            if j < N-1 and i < N-1 and not board[i+1][j+1]:
                dp[i + 1][j + 1][2] += dp[i][j][2]

pprint(dp)
print(dp[N-1][N-1])


