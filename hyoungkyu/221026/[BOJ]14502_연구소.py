# 골드4 / 3368ms
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

D = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs():
    global minV
    que = deque()
    for i in virus:
        que.append(i)
        visited[i[0]][i[1]] = 1
    flag = False
    cnt = 0
    while que:
        i, j = que.popleft()
        for di, dj in D:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                que.append([ni, nj])
                visited[ni][nj] = 1
                cnt += 1
            if cnt > minV:
                flag = True
                break
        if flag:
            break
    if minV > cnt:
        minV = cnt
        # wall = [a, b, c, d, e, f]
        # walls.append(sorted(wall))


N, M = map(int, input().split())
arr = []
number = [0, 0, 0]
virus = []
zero = 0
for i in range(N):
    arr_tmp = list(map(int, input().split()))
    for j in range(M):
        if arr_tmp[j] == 2:
            number[2] += 1
            virus.append([i, j])
        elif arr_tmp[j] == 0:
            zero += 1
    arr.append(arr_tmp[:])

minV = zero

flag = False

# walls = []

for a in range(N):
    for b in range(M):
        if arr[a][b] == 0:
            arr[a][b] = 1
        
            for c in range(a, N):
                for d in range(M):
                    if arr[c][d] == 0:    
                        arr[c][d] = 1

                        for e in range(c, N):
                            for f in range(M):
                                if arr[e][f] == 0:
                                    arr[e][f] = 1
                                    # tmp = [a, b, c, d, e, f]
                                    # if sorted(tmp) not in walls:
                                    visited = [[0]*M for _ in range(N)]
                                    bfs()
                                    arr[e][f] = 0
                        arr[c][d] = 0
            arr[a][b] = 0

print(zero-minV-3)


