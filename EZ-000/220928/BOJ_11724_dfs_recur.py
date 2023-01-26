import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# dfs 함수 정의
def dfs(v, visited):
    global result
    visited[v] = 1
    result.append(v)
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(vertex, visited)


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
while graph.keys():
    visited = [0] * (N + 1)
    start = list(graph.keys())[0]
    result = []
    dfs(start, visited)
    cnt += 1

    for v in result:
        if v in graph.keys():
            del graph[v]

print(cnt)
