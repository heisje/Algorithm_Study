# 골드4 / 92ms
import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
visited = [[0] * N for _ in range(N)]
body = deque()

# L : 왼쪽으로 90도 회전, D : 오른쪽으로 90도 회전
D = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우하좌상
Direction = []
for _ in range(int(input())):
    X, C = input().split()
    Direction.append([int(X), C])       # X : 시간, C : 회전 방향

visited[0][0] = 1
body.append([0, 0])                     # 움직이는 위치가 body에 없고 벽이 아니면 추가하고 body의 첫번째 원소를 pop
cnt = 0                                 # 시간 변수
direction = 0                           # 처음에 오른쪽으로 이동
ni, nj = 0, 0                           # 초기 위치

while True:
    cnt += 1
    
    ni, nj = ni+D[direction][0], nj+D[direction][1]
    if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
        if arr[ni][nj] == 1:
            visited[ni][nj] = 1
            body.append([ni, nj])
            arr[ni][nj] = 0
        else:
            i, j = body.popleft()
            visited[i][j] = 0
            body.append([ni, nj])
            visited[ni][nj] = 1
    else:
        break

    if Direction and cnt == Direction[0][0]:
        if Direction[0][1] == 'L':
            direction = (direction + 4 - 1) % 4
        else:
            direction = (direction + 1) % 4
        Direction.pop(0)

print(cnt)
