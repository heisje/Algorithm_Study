import sys
input = lambda :sys.stdin.readline().strip()
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, i, j):
    count = 0
    while arr[x+i][y+j] != '#' and arr[x][y] != 'O':                        # 이동할 수 있을 때 까지
        x += i                                                              # 같은 방향으로 계속 반복
        y += j
        count += 1                                                          # 각 구슬이 몇 번 갔는지 계산
    return x, y, count

def bfs():
    q = deque()
    visited = []
    q.append((red_sx, red_sy, blue_sx, blue_sy, 1))
    cnt = 0
    while q:
        red_x, red_y, blue_x, blue_y, cnt = q.popleft()

        if cnt > 10:                                                        # 10번 넘어가면 멈추고 -1 return
            break

        for i in range(4):                                                  # 4 방향으로 탐색
            red_nx, red_ny, red_cnt = move(red_x, red_y, dx[i], dy[i])
            blue_nx, blue_ny, blue_cnt = move(blue_x, blue_y, dx[i], dy[i])

            if arr[blue_nx][blue_ny] == 'O':                                # 파란 구슬이 구멍에 들어가면
                continue                                                    # 무시하고 계속

            if arr[red_nx][red_ny] == 'O':                                  # 빨간 구슬이 구멍에 들어가면
                return cnt                                                  # 횟수 return

            if red_nx == blue_nx and red_ny == blue_ny:                     # 빨간 구슬과 파란 구슬이 같은 위치일 때
                if red_cnt > blue_cnt:                                      # cnt가 많은게 더 늦게 도착했으므로 한 칸 전으로
                    red_nx -= dx[i]
                    red_ny -= dy[i]
                else:
                    blue_nx -= dx[i]
                    blue_ny -= dy[i]

            if [red_nx, red_ny, blue_nx, blue_ny] not in visited:           # 방문하지 않았으면
                visited.append([red_nx, red_ny, blue_nx, blue_ny])          # visited에 추가
                q.append((red_nx, red_ny, blue_nx, blue_ny, cnt + 1))       # q에 추가
    return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 각 구슬 좌표 구하기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            red_sx, red_sy = i, j
        elif arr[i][j] == 'B':
            blue_sx, blue_sy = i, j

print(bfs())