# 골드5 / 40ms
import sys

input = lambda:sys.stdin.readline().strip()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [list([0, 0, 0] for _ in range(N)) for _ in range(N)]
# print(memo)
memo[0][1][0] = 1

# status -> 0 : 가로, 1 : 대각선, 2 : 세로

for i in range(N):
    for j in range(1, N):
        if arr[i][j]:
            continue
        # 가로 = 왼쪽에 가로, 대각선으로 놓여있는 경우
        memo[i][j][0] += memo[i][j-1][0] + memo[i][j-1][1]

        if i == 0: continue
        # 대각선 = 왼쪽 위에 가로, 세로, 대각선으로 놓여있는 경우
        if not arr[i-1][j-1] and not arr[i][j-1] and not arr[i-1][j]:
            memo[i][j][1] += sum(memo[i-1][j-1])

        # 세로 = 위에 대각선, 세로로 놓여있는 경우
        memo[i][j][2] += memo[i-1][j][1] + memo[i-1][j][2]

print(sum(memo[N-1][N-1]))