# 골드3 / 76ms
import sys
input = lambda:sys.stdin.readline().strip()

D = [[-1, 0], [0, -1], [0, 1], [1, 0]]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            ni, nj = i, j

size = 2                            # 상어의 크기
hunt = 0                            # 잡은 물고기 수(size 증가시킬 때 필요)
time = 0
flag = False                        # 더 이상 잡아먹을 수 있는 사이즈가 없으면 break시킬 변수
q = []
q.append([ni, nj])
tmp = []
hunting = []
visited = [[0] * N for _ in range(N)]
visited[ni][nj] = 0
lst[ni][nj] = 0
result = 0
while q:
    ni, nj = q.pop(0)
    for di, dj in D:
        if 0<=ni+di<N and 0<=nj+dj<N and lst[ni+di][nj+dj] <= size and visited[ni+di][nj+dj] == 0:      # 지나갈 수 있으면
            if 0 < lst[ni+di][nj+dj] < size:                                                            # 물고기가 있고 먹을 수 있으면
                hunting.append([ni+di, nj+dj])
            visited[ni+di][nj+dj] = visited[ni][nj] + 1
            tmp.append([ni+di, nj+dj])

    if q == []:
        if hunting != []:
            hunting.sort()
            ki, kj = hunting[0]
            hunt += 1
            if hunt == size:
                size += 1
                hunt = 0
            result += visited[ki][kj]
            visited = [[0] * N for _ in range(N)]
            q = []
            tmp = []
            hunting = []
            lst[ki][kj] = 0
            tmp.append([ki, kj])
            time = 0
        
        if tmp:
            q = tmp[:]
        tmp = []
print(result)