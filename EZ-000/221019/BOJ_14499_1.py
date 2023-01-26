import sys
input = sys.stdin.readline


N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
order = list(map(int, input().split()))

delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dice_num = {n: 0 for n in range(1, 7)}
dice_arr = [1, 2, 3, 4, 5, 6]
delta_dice = {
    1: (3, 1, 2, 5, 0, 4),
    2: (4, 1, 2, 0, 5, 3),
    3: (2, 0, 5, 3, 4, 1),
    4: (1, 5, 0, 3, 4, 2)
    }
upside = 1
for o in order:
    nextX = x + delta[o][0]
    nextY = y + delta[o][1]

    if nextX < 0 or N - 1 < nextX or nextY < 0 or M - 1 < nextY:
        continue
    else:
        temp = [0] * 6
        x = nextX
        y = nextY
        d = delta_dice[o]
        for n in range(6):
            temp[n] = dice_arr[d[n]]
        dice_arr = temp[:]
        upside = dice_arr[0]
        bottom = dice_arr[-1]
        if board[x][y]:
            dice_num[bottom] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice_num[bottom]
        print(dice_num[upside])
