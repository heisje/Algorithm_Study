N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, M):
    board[0][i] += board[0][i-1]

for i in range(1, N):
    left = [board[i][j] + board[i - 1][j] for j in range(M)]
    right = [board[i][j] + board[i - 1][j] for j in range(M)]

    for j in range(1, M):
        left[j] = max(left[j], left[j-1] + board[i][j])

    for j in range(M-2, -1, -1):
        right[j] = max(right[j], right[j+1] + board[i][j])

    for j in range(M):
        board[i][j] = max(left[j], right[j])

print(board[N-1][M-1])

