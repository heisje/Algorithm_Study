import sys
input = sys.stdin.readline

def dfs(cnt, idx):
    global min_
    if cnt == N // 2:                                   # 팀 나눴으면
        start, link = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if visited[i] and visited[j]:           # visited == 1이면 스타트팀
                    start += (arr[i][j] + arr[j][i])    # 능력치 구하기
                elif not visited[i] and not visited[j]: # link 팀
                    link += (arr[i][j] + arr[j][i])
        min_ = min(min_, abs(start - link))             # 최솟값 갱신
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1              # start 팀
            dfs(cnt + 1, i + 1)         # 재귀
            visited[i] = 0



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_ = float('inf')

dfs(0, 0)
print(min_)

