import sys
sys.setrecursionlimit(10**6)

N = int(input())
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(x, y, color, count): #안 색맹용
    for i in range(4):
        if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N : #사각형 속
            if arr[y+dy[i]][x+dx[i]] in color and vis_RGB[y+dy[i]][x+dx[i]] == 0: #방문 안했으면
                vis_RGB[y+dy[i]][x+dx[i]] = count
                dfs(x+dx[i], y+dy[i], color, count)
def dfs2(x, y, color, count):# 색맹용
    for i in range(4):
        if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N : #사각형 속
            if arr[y+dy[i]][x+dx[i]] in color and vis_RB[y+dy[i]][x+dx[i]] == 0: #방문 안했으면
                vis_RB[y+dy[i]][x+dx[i]] = count
                dfs2(x+dx[i], y+dy[i], color, count)

arr = [list(input())for _ in range(N)]
vis_RGB = [[0] * N for _ in range(N)] #안색맹
vis_RB = [[0] * N for _ in range(N)]  #색맹

count = 1
for y in range(N):
    for x in range(N):
        if arr[y][x] == 'R' and vis_RGB[y][x] == 0: #R은 R끼리
            dfs(x, y, ['R'], count)
            count += 1
            continue
        elif arr[y][x] == 'G' and vis_RGB[y][x] == 0: #G는 G끼리
            dfs(x, y, ['G'], count)
            count += 1
            continue
        elif arr[y][x] == 'B' and vis_RGB[y][x] == 0: #B는 B끼리
            dfs(x, y, ['B'], count)
            count += 1
            continue
print(count - 1, end=" ")
count = 1
for y in range(N):
    for x in range(N):
        if (arr[y][x] == 'R' or arr[y][x] == 'G') and vis_RB[y][x] == 0: #R은 R, G끼리
            dfs2(x, y, ['R', 'G'], count)
            count += 1
            continue
        elif arr[y][x] == 'B' and vis_RB[y][x] == 0: # B는 B끼리
            dfs2(x, y, ['B'], count)
            count += 1
            continue
print(count - 1)

#골드 5 / 15분 / 124ms