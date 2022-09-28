import sys
input = lambda :sys.stdin.readline()
sys.setrecursionlimit(10001)

def dfs(n):
    for node in nodes[n]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node)


N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for m in range(M):
    start, end = map(int, input().split())
    nodes[start].append(end)
    nodes[end].append(start)

count = 0
for n in range(1, N+1):
    if visited[n] == 0:
        count += 1
        visited[n] = 1
        dfs(n)
print(count)
#실버2 / 40분 / 932ms