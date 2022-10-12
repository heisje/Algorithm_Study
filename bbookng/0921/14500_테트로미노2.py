import sys
input = lambda :sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

result = 0
_max = max([max(line) for line in arr])                         # 가지치기를 위한 arr 내의 최댓값 찾기

def dfs(i, j, cnt, tmp):
    global result
    if tmp + (4 - cnt) * _max < result:                         # 현재 tmp + 남은 값에 최댓값 더해도 현재 최댓값 보다 작다면
        return                                                  # 가지치기
    if cnt == 4:                                                # 4번 돌았으면
        if tmp > result:                                        # 최댓값 갱신
            result = tmp
            return

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:           # 델타 탐색
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if cnt == 2:                                        # 2번째에서 방향 꺾일 수 있으니까
                visited[nx][ny] = 1                             # 방문처리
                dfs(i, j, cnt+1, tmp + arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, tmp + arr[nx][ny])
            visited[nx][ny] = 0

for i in range(N):                                              # 좌표마다 돌아주기
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(result)
