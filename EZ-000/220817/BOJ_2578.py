import sys

board = []
numbers = []

for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
    temp = list(map(int, sys.stdin.readline().split()))
    for idx in range(5):
        numbers.append(temp[idx])

# 사회자가 부른 수를 0으로 바꾸기
for idx in range(len(numbers)):
    bingo = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == numbers[idx]:
                board[i][j] = 0
    
    # 가로 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[i][j] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1

    # 세로 체크
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[j][i] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1
    
    # 대각선 체크
    cnt1 = 0
    cnt2 = 0
    for i in range(5):
        if board[i][i] == 0:
            cnt1 += 1
        if board[i][4 - i] == 0:
            cnt2 += 1
    if cnt1 == 5:
        bingo += 1
    if cnt2 == 5:
        bingo += 1

    # BINGO!
    if bingo >= 3:
        print(idx + 1)
        break
