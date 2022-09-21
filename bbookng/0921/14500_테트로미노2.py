import sys
input = lambda :sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

result = 0
_max = max([max(line) for line in arr])

def dfs(i, j, cnt, tmp):
    global result
    if tmp + (4 - cnt) * _max < result:
        return
    if cnt == 4:
        if tmp > result:
            result = tmp
            return

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(i, j, cnt+1, tmp + arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, tmp + arr[nx][ny])
            visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(result)

