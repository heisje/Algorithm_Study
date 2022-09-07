# 골드 5 / 164ms
import queue
import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
lst = [list(input()) for _ in range(N)]
visited1 = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cnt1 = cnt2 = 0                             # cnt1 : 정상, cnt2 : 적록색약
queue1 = []
queue2 = []
for i in range(N):
    for j in range(N):
        # 정상인
        if visited1[i][j] == 0:
            visited1[i][j] = 1
            queue1.append([i, j])
            cnt1 += 1
            while queue1:
                ni, nj = queue1.pop(0)
                for di, dj in D:
                    if 0<=ni+di<N and 0<=nj+dj<N and visited1[ni+di][nj+dj]==0 and lst[ni+di][nj+dj] == lst[ni][nj]:
                        visited1[ni+di][nj+dj] = 1
                        queue1.append([ni+di, nj+dj])
        # 적록색약
        if visited2[i][j] == 0:
            visited2[i][j] = 1
            queue2.append([i, j])
            cnt2 += 1
            while queue2:
                ni, nj = queue2.pop(0)
                for di, dj in D:
                    if lst[ni][nj] == 'R' or lst[ni][nj] == 'G':
                        if 0<=ni+di<N and 0<=nj+dj<N and visited2[ni+di][nj+dj]==0 and (lst[ni+di][nj+dj] == 'R' or lst[ni+di][nj+dj] == 'G'):
                            visited2[ni+di][nj+dj] = 1
                            queue2.append([ni+di, nj+dj])
                    else:
                        if 0<=ni+di<N and 0<=nj+dj<N and visited2[ni+di][nj+dj]==0 and lst[ni+di][nj+dj] == 'B':
                            visited2[ni+di][nj+dj] = 1
                            queue2.append([ni+di, nj+dj])

print(cnt1, cnt2)               