import sys
input = sys.stdin.readline


# dfs 함수 정의
def dfs(v, result):
    global visited
    visited += [v]
    stack = [v]
    while stack:
        now = stack.pop()
        for node in graph[now]:
            if node not in visited:
                visited += [node]
                stack.append(node)
    return


# 연결 정보를 dict graph에 저장
N, M = map(int, input().split())
graph = {n: [] for n in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    if u in graph.keys():
        graph[u] += [v]
        graph[v] += [u]
    else:
        graph[u] = [v]
        graph[v] = [u]

# graph에 key가 남아있는 동안 dfs 탐색
# dfs가 한 번 끝날 때마다 cnt 증가
cnt = 0
visited = []
while len(visited) < N:
    for idx in range(1, N + 1):
        if idx not in visited:
            start = idx
            break
    dfs(start, [])
    cnt += 1
print(cnt)
