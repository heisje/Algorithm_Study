from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())

arr = deque(deque(deque() for _ in range(N)) for _ in range(H)) #이것도 데큐로...
for h in range(H):
    for n in range(N):
        arr[h][n] = deque(map(int, sys.stdin.readline().split())) #이것도 데큐로...

# 벡터 탐색
vM = (-1, 1, 0, 0, 0, 0)
vN = (0, 0, -1, 1, 0, 0)
vH = (0, 0, 0, 0, -1, 1)
qu = deque()

all = M * N * H
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1: #숫자가 맞으면
                qu.append((h, n, m))
            if arr[h][n][m] != 0: #총 숫자의 갯수세기 -1, 1 경우
                all -= 1

mx = 1
while qu:
    h, n, m = qu.popleft()
    for i in range(0, 6): #벡터검색
        if 0 <= m + vM[i] < M and 0 <= n + vN[i] < N and 0 <= h + vH[i] < H: #방향측정
            if arr[h + vH[i]][n + vN[i]][m + vM[i]] == 0: #visited 안갔냐
                arr[h + vH[i]][n + vN[i]][m + vM[i]] = arr[h][n][m] + 1 #visited 갔다
                all -= 1 #총 숫자의 갯수세기 0일 경우
                if mx < arr[h][n][m] + 1: #최대값
                    mx = arr[h][n][m] + 1
                qu.append((h + vH[i],  n + vN[i], m + vM[i])) # queue에 넣기

if all == 0:  #총 숫자의 갯수가 맞으면
    print(mx-1)
else:   #총 숫자의 갯수가 안맞으면
    print(-1)

#pypy / 골드5 / 812ms / 1시간