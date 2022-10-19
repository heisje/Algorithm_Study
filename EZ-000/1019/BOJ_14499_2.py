N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
order = list(map(int, input().split()))

delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dice_num = {n: 0 for n in range(1, 7)}  # 주사위에 적힌 숫자
dice_arr = [1, 2, 5, 4, 3, 6]           # 현재 주사위 인덱스 = [위, 상, 하, 좌, 우, 아래]
delta_dice = {                          # delta_dice = { 이동 방위: 변경 인덱스 }
    1: (3, 1, 2, 5, 0, 4),              # 동
    2: (4, 1, 2, 0, 5, 3),              # 서
    3: (2, 0, 5, 3, 4, 1),              # 북
    4: (1, 5, 0, 3, 4, 2)               # 남
    }
upside = 1
for o in order:
    nextX = x + delta[o][0]                 # 다음 칸 x 좌표
    nextY = y + delta[o][1]                 # 다음 칸 y 좌표
    # 지도 바깥이면 명령 무시
    if nextX < 0 or N - 1 < nextX or nextY < 0 or M - 1 < nextY:
        continue
    else:
        temp = [0] * 6                      # 변경 인덱스 임시 저장 리스트
        x, y = nextX, nextY
        d = delta_dice[o]                   # 주사위 인덱스 변경
        for n in range(6):
            temp[n] = dice_arr[d[n]]
        dice_arr = temp[:]
        upside = dice_arr[0]
        bottom = dice_arr[-1]
        if board[x][y]:                     # 지도의 숫자가 0이 아니면
            dice_num[bottom] = board[x][y]      # 밑면에 지도의 숫자를 복사
            board[x][y] = 0                     # 지도의 숫자를 0으로 변경
        else:                               # 지도의 숫자가 0이면
            board[x][y] = dice_num[bottom]      # 밑면의 숫자를 지도에 복사
        print(dice_num[upside])             # 윗면의 숫자 출력
