import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))


dice = [0] * 6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def update(direction, dice):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice = [d, b, a, f, e, c]
    elif direction == 2:
        dice = [c, b, f, a, e, d]
    elif direction == 3:
        dice = [e, a, c, d, f, b]
    elif direction == 4:
        dice = [b, f, c, d, a, e]
    return dice


for i in order:
    x, y = x + dx[i], y + dy[i]
    if 0 <= x < N and 0 <= y < M:
        dice = update(i, dice)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])
    else:
        x, y = x - dx[i], y - dy[i]