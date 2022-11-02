import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

def vacuum(x, y, z):
    global d
    clean = deque()
    clean.append((x, y, z))
    visited[x][y] = 1

    while clean:
        i, j, c = clean.pop()

        for di, dj in D:
            ni, nj = i + di, j + dj
            if place[ni][nj] == 0 and visited[ni][nj] == 0:               # 청소 가능한 곳이 하나라도 있으면 break
                break
        else:                                                             # 청소 가능한 곳이 없으면
            b = (d - 2) if d > 1 else (d + 2)
            bi, bj = i + D[b][0], j + D[b][1]                             # 후진할 좌표 설정

            if place[bi][bj] == 1:                                        # 후진할 곳이 벽이면 return
                return c
            else:
                clean.append((bi, bj, c))                                 # 벽이 아니면 후진하기 위해 append

            continue

        d = (d + 3) % 4                                                   # 방향 회전
        ni, nj = i + D[d][0], j + D[d][1]

        if place[ni][nj] == 0 and visited[ni][nj] == 0:                   # 왼쪽에 청소 가능한 곳이 있다면
            clean.append((ni, nj, c+1))                                   # 청소한 칸의 개수 더해주고 append
            visited[ni][nj] = 1
        else:                                                             # 왼쪽에 청소 가능한 곳이 없다면
            clean.append((i, j, c))                                       # 좌표 그대로 append (방향만 바뀜.)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]                                    # 북 동 남 서

print(vacuum(r, c, 1))