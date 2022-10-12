# 골드1 / 88ms
import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 상, 하, 좌, 우
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Red = [i, j]
        elif arr[i][j] == 'B':
            Blue = [i, j]

def _moveBall(x, y, direction):
    cx, cy = x, y
    cnt = 0
    while True:
        nx, ny = cx + D[direction][0], cy + D[direction][1]             # 공 움직이기
        if arr[nx][ny] != '#':                                          # 벽을 만날때까지 이동
            cnt += 1                                                    # 이동 횟수 카운트
            cx, cy = nx, ny                                             # 한칸씩 이동
            if arr[nx][ny] == 'O':                                      # 구멍에 빠지면 break
                break
        else:                                                           # 벽을 만나면 break
            break
    return cx, cy, cnt

def moveBall(redX, redY, blueX, blueY, direction):
    n_redX, n_redY, cnt_red = _moveBall(redX, redY, direction)
    n_blueX, n_blueY, cnt_blue = _moveBall(blueX, blueY, direction)
    if n_redX == n_blueX and n_redY == n_blueY:                         # 움직인 후의 위치가 같은 경우
        if arr[n_redX][n_redY] != 'O':                                  # 구멍에 빠지지 않는 경우
            if cnt_red < cnt_blue:                                      # 이동 횟수로 위치 조정
                n_blueX -= D[direction][0]
                n_blueY -= D[direction][1]
            else:
                n_redX -= D[direction][0]
                n_redY -= D[direction][1]
        else:                                                           # 구멍에 동시에 빠지는 경우
            return redX, redY, blueX, blueY                             # 해당 방향으로 움직이지 않기
    else:                                                               # 움직인 후의 위치가 같지 않은 경우
        if arr[n_blueX][n_blueY] == 'O':                                # 파란 공이 구멍에 빠지면
            return redX, redY, blueX, blueY                             # 해당 방향으로 움직이지 않기
    return n_redX, n_redY, n_blueX, n_blueY

que = deque()                                                           # bfs
que.append([Red[0], Red[1], Blue[0], Blue[1], []])
cnt = 1
tmp = deque()
visited = deque()
good = False                                                            # 구슬 빼내기에 성공을 나타내는 변수!!!!
while cnt <= 10 and que:
    redX, redY, blueX, blueY, s = que.popleft()
    for i in range(4):
        n_redX, n_redY, n_blueX, n_blueY = moveBall(redX, redY, blueX, blueY, i)
        if arr[n_redX][n_redY] == 'O':
            good = True
            s += [i]
            break
        if [n_redX, n_redY, n_blueX, n_blueY] not in visited:
            tmp.append([n_redX, n_redY, n_blueX, n_blueY, s+[i]])
            visited.append([n_redX, n_redY, n_blueX, n_blueY])
    if good:
        break
    if que == deque() and tmp != deque():
        que = tmp
        cnt += 1
        tmp = deque()
if good:
    print(cnt)
else:
    print(-1)