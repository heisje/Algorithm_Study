import sys
from collections import deque

input = sys.stdin.readline

global N
global answer
answer = 0


def no_diagonal(x, y, status):
    global answer
    if (x, y) not in visited:
        if -1 < x < N and -1 < y < N and not wall[x][y]:
            if (x, y) == (N - 1, N - 1):
                answer += 1
            else:
                que.append((x, y, status))
                visited.add((x, y, status))


def diagonal(px, py):
    global answer
    r1, c1 = px + dr[0], py + dc[0]
    r2, c2 = px + dr[1], py + dc[1]
    r3, c3 = px + dr[2], py + dc[2]

    if (r3, c3) not in visited:
        con1 = -1 < r1 < N and -1 < c1 < N and not wall[r1][c1]
        con2 = -1 < r2 < N and -1 < c2 < N and not wall[r2][c2]
        con3 = -1 < r3 < N and -1 < c3 < N and not wall[r3][c3]
        if con1 and con2 and con3:
            if (r3, c3) == (N - 1, N - 1):
                answer += 1
            else:
                que.append((r3, c3, 2))
                visited.add((r3, c3, 2))


N = int(input())
wall = [list(map(int, input().split())) for _ in range(N)]
que = deque([(0, 1, 0)])
visited = {(0, 1, 0)}
dr = (0, 1, 1)
dc = (1, 0, 1)

if not wall[N - 1][N - 1]:
    while que:
        r, c, s = que.popleft()
        if s < 2:
            sr, sc = r + dr[s], c + dc[s]
            no_diagonal(sr, sc, s)
            diagonal(r, c)

        else:
            hr, hc = r + dr[0], c + dc[0]
            vr, vc = r + dr[1], c + dc[1]
            no_diagonal(hr, hc, 0)
            no_diagonal(vr, vc, 1)
            diagonal(r, c)

print(answer)
