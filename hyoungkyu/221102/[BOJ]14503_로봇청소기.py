# 골드5 / 72ms
import sys
input = lambda:sys.stdin.readline().strip()

# 인덱스 조작 개짜증나게 해놨네;;
# d = 0, 1, 2, 3 --> 북, 동, 남, 서
# 무조건 왼쪽부터 청소할 곳을 찾아야됨 --> 4방향 탐색 범위를 for i in range(1, 5)로 해야됨
D = [[-1, 0], [0, -1], [1, 0], [0, 1]]     # 북서남동 --> 왼쪽으로 돌리기 위해 북동남서가 아니라 북서남동

N, M = map(int, input().split())

r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
stack = []
cnt = 1
if d == 1:
    d = 3
elif d == 3:
    d = 1
def dfs(i, j, d):
    global cnt
    visited[i][j] = 1
    while True:
        for k in range(1, 5):
            ni, nj = i+D[(d+k)%4][0], j+D[(d+k)%4][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                flag = False
                visited[ni][nj] = 1
                cnt += 1
                i, j, d = ni, nj, (d+k)%4
                break
        else:
            ni, nj = i-D[d][0], j-D[d][1]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                i, j = ni, nj
            else:
                return cnt
dfs(r, c, d)
print(cnt)
