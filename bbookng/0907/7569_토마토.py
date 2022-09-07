import sys
from collections import deque
input = lambda :sys.stdin.readline().strip()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():                              # 그냥 우리가 아는.. bfs...
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and board[nz][nx][ny] == 0:  # 안익었으면
                q.append((nx, ny, nz))
                board[nz][nx][ny] = board[z][x][y] + 1



M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque([])

for i in range(H):                          # 도마도가 들어있는 위치 찾아서 큐에 넣어주기
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((j, k, i))

bfs()                                       # 함수 실행

result = 0                                  

for i in board:
    for j in i:
        if j.count(0) > 0:                  # 안익은게 하나라도 있으면
            print(-1)                       # 도마도 숙성 실패
            exit()                          # 바로 종료
        else:                               
            result = max(result, max(j))    # 가장 나중에 익은 도마도 찾기

print(result-1)                             # 익은 도마도가 1부터 시작하기 때문에 -1 해조야함