import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 다음 상하좌우 가능한 위치 찾기
def pos(r, c, depth):
    depth += 1
    new = []
    for D in delta:
        dist, flag = far(r, c, D)
        new_pos = (r + D[0] * dist, c + D[1] * dist)
        new.append([new_pos, depth, flag, dist, D])
    return new


# 얼마나 멀리 전진 가능한가?
def far(r, c, d):
    f = 0
    flag = 0
    while True:
        f += 1
        p = board[r + d[0] * f][c + d[1] * f]
        if p == '#':
            f = f - 1
            break
        elif p == 'O':
            flag = 1
            break
    return f, flag


def bfs():
    rq = deque([[R, 0, 0, 0, (0, 0)]])
    bq = deque([[B, 0, 0, 0, (0, 0)]])
    while rq:
        temp_r = rq.popleft()
        temp_b = bq.popleft()
        rr = temp_r[0][0]
        rc = temp_r[0][1]
        br = temp_b[0][0]
        bc = temp_b[0][1]
        depth = temp_r[1]
        flag_r = temp_r[2]
        flag_b = temp_b[2]
        dist_r = temp_r[3]
        dist_b = temp_b[3]
        dir_r = temp_r[4]
        dir_b = temp_b[4]
        # print(rr, rc, flag_r, depth)
        # print(br, bc, flag_b)
        if 10 < depth:
            return -1
        elif flag_r and not flag_b:
            return depth
        else:
            if rr == br and rc == bc:
                if dist_r < dist_b:
                    br += -dir_b[0]
                    bc += -dir_b[1]
                else:
                    rr += -dir_r[0]
                    rc += -dir_r[1]
            for row in range(N):
                for col in range(M):
                    if board[row][col] in ['.', 'R', 'B']:
                        board[row][col] = '.'
            if (rr, rc) != O:
                board[rr][rc] = 'R'
            if (br, bc) != O:
                board[br][bc] = 'B'

            # for l in board:
            #     print(l)
            news_r = pos(rr, rc, depth)
            news_b = pos(br, bc, depth)
            rq.extend(news_r)
            bq.extend(news_b)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = (i, j)
        if board[i][j] == 'B':
            B = (i, j)
        if board[i][j] == 'O':
            O = (i, j)

visited = {}
print(bfs())
