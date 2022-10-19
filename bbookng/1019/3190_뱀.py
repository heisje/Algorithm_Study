import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * (N+2) for _ in range(N+2)]

for _ in range(K):                                          # 사과의 위치
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())
turn = dict()                                               # 방향 변환 정보를 담을 dictionary

for _ in range(L):
    X, C = input().split()
    turn[int(X)] = C

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((1, 1))                                            # 시작 위치

x, y = 1, 1
cnt = 0
i = 0

while q:
    cnt += 1

    x, y = x + dx[i], y + dy[i]
    if not 1 <= x <= N or not 1 <= y <= N or (x, y) in q:   # 범위를 벗어나거나 이미 뱀의 몸이라면
        break

    q.append((x, y))                                        # 머리를 다음칸에 위치 시킨다

    if board[x][y]:                                         # 사과가 있으면
        board[x][y] = 0                                     # 사과 먹었다고 표시, 꼬리 움직이지 않음
    else:                                                   # 사과 없으면
        q.popleft()                                         # 꼬리를 땡겨서 몸 길이 줄이기

    if cnt in turn:                                         # 방향 변환 때가 되면
        if turn[cnt] == 'D':                                # D 이면 오른쪽으로 90도
            i = (i + 1) % 4
        else:                                               # L 이면 왼쪽으로 90도
            i = (i - 1) % 4
print(cnt)