# 72ms
import sys
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
K = int(input())

D = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 북남서동
lst = [[-1] * (N+1) for _ in range(M+1)]
for i in range(1, M):
    lst[i][0] = 0
    lst[i][N] = 0
lst[0] = [0] * (N+1)
lst[M] = [0] * (N+1)

stack = []
for k in range(1, K+1):
    di, pos = map(int, input().split())
    if di == 1:
        lst[0][pos] = k
        stack.append([0, pos])
    elif di == 2:
        lst[M][pos] = k
        stack.append([M, pos])
    elif di == 3:
        lst[pos][0] = k
        stack.append([pos, 0])
    elif di == 4:
        lst[pos][N] = k
        stack.append([pos, N])

di, pos = map(int, input().split())
if di == 1:
    x, y = 0, pos
elif di == 2:
    x, y = [M, pos]
elif di == 3:
    x, y = [pos, 0]
elif di == 4:
    x, y = [pos, N]

ni, nj = x, y
cnt = -1

check = [[0] * (N+1) for _ in range(M+1)]
while True:
    for di, dj in D:
        if 0<=ni+di<=M and 0<=nj+dj<=N and (lst[ni+di][nj+dj] != -1 or check[ni+di][nj+dj] == N+M):
            cnt += 1
            lst[ni][nj] = -1
            if cnt == N+M:
                check[ni][nj] = cnt
                ni, nj = x, y
                cnt = -1
                break
            check[ni][nj] = cnt
            ni += di
            nj += dj
            break
    else:
        break

tot = 0
for k in stack:
    i, j = k
    tot += check[i][j]
print(tot)