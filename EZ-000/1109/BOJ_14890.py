import sys
input = sys.stdin.readline


def slope(board):
    cnt = 0
    slopes = [[0] * N for _ in range(N)]
    for r in range(N):
        flag = 1
        for c in range(N - 1):
            now, nex = board[r][c], board[r][c + 1]
            if now < nex:
                for n in range(L):
                    if nex - now != 1 or c - n < 0 or slopes[r][c - n] or board[r][c] != board[r][c - n]:
                        flag = 0
                        break
                    else:
                        slopes[r][c - n] = 1
            elif now > nex:
                for n in range(L):
                    if now - nex != 1 or N - 1 < c + n + 1 or slopes[r][c + n + 1] or board[r][c + 1] != board[r][c + n + 1]:
                        flag = 0
                        break
                    else:
                        slopes[r][c + n + 1] = 1
        if flag:
            cnt += 1
    return cnt


N, L = map(int, input().split())
B1 = []
for _ in range(N):
    B1.append(list(map(int, input().split())))
B2 = list(zip(*B1))

print(slope(B1) + slope(B2))
