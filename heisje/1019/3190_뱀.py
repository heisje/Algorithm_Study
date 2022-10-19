import sys
input = lambda: sys.stdin.readline()
from collections import deque

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))  # x, y

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    y, x = map(int, input().split())
    apples.append((x - 1, y - 1))
L = int(input())
rotates = deque()
for _ in range(L):
    time, turn = input().split()
    rotates.append((int(time), turn))

time = 0   # 현재시간
pre_d = 3  # 현재방향
pre_x = 0  # 현재위치
pre_y = 0
g_visit = [[1 for _ in range(N)] for _ in range(N)]  # 뱀그림
for x, y in apples:
    g_visit[y][x] = 7  # 사과가 있으면 7
g_visit[0][0] = 0  # 뱀이 지나간 자리는 0
snake = deque()  # 뱀 위치를 누적 저장
snake.append((0,0))
while True:
    # 타임에 맞으면 돌리기
    if rotates:
        if time == rotates[0][0]:
            _, turn = rotates.popleft()
            if turn == 'L':
                pre_d = (pre_d + 1) % 4
            elif turn == 'D':
                pre_d = (pre_d - 1) % 4
    
    # 이동하기
    go_x = pre_x + delta[pre_d][0]
    go_y = pre_y + delta[pre_d][1]

    # 이동 할 곳이 벽이면 끝
    if go_x < 0 or N <= go_x or go_y < 0 or N <= go_y:
        print(time+1)
        exit()
    # 이동 할 곳이 뱀이면 끝
    if g_visit[go_y][go_x] == 0:
        print(time+1)
        exit()

    # 이동 할 곳에 사과가 있으면
    if g_visit[go_y][go_x] == 7:
        pass
    # 비어있으면
    elif g_visit[go_y][go_x] == 1:
        x, y = snake.popleft()
        g_visit[y][x] = 1
    g_visit[go_y][go_x] = 0
    snake.append((go_x, go_y))
    pre_x, pre_y = go_x, go_y
    time += 1

# 골드4 / 1시간