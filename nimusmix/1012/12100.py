from copy import deepcopy
import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
real_board = [list(map(int, input().split())) for _ in range(N)]
maxV = 0

def dfs(cnt, board):
    global maxV
    if cnt == 5:
        maxF = max(map(max, board))
        if maxF > maxV:
            maxV = maxF
        return
    
    for i in range(4):
        t_board = deepcopy(board)
        dfs(cnt+1, move(i, t_board))
    
def move(n, board):
    # 상
    if n == 0:
        for j in range(N):
            last = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if board[last][j] == 0:
                        board[last][j] = tmp
                    elif board[last][j] == tmp:
                        board[last][j] += tmp
                        last += 1
                    else:
                        last += 1
                        board[last][j] = tmp
    # 하
    elif n == 1:
        for j in range(N):
            last = N - 1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if board[last][j] == 0:
                        board[last][j] = tmp
                    elif board[last][j] == tmp:
                        board[last][j] += tmp
                        last -= 1
                    else:
                        last -= 1
                        board[last][j] = tmp
    # 좌
    elif n == 2:
        for i in range(N):
            last = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if board[i][last] == 0:
                        board[i][last] = tmp
                    elif board[i][last] == tmp:
                        board[i][last] += tmp
                        last += 1
                    else:
                        last += 1
                        board[i][last] = tmp
    # 우
    else:
        for i in range(N):
            last = N - 1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    
                    if board[i][last] == 0:
                        board[i][last] = tmp
                    elif board[i][last] == tmp:
                        board[i][last] += tmp
                        last -= 1
                    else:
                        last -= 1
                        board[i][last] = tmp
    return board

dfs(0, real_board)
print(maxV)