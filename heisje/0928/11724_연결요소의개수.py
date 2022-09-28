import sys
input = lambda :sys.stdin.readline()
N, M = map(int, input().split())
nodes = [[] for _ in range(N)]
visited = [0] * N
for m in range(M):
    start, end = map(int, input().split())
    nodes[start-1].append(end-1)
    nodes[end-1].append(start-1)


count = 0
for n in range(N):
    if visited[n] == 0:
        count += 1
        visited[n] = 1
        stack = [n]
        while stack:
            n = stack.pop()
            for node in nodes[n]:
                if visited[node] == 0:
                    visited[node] = 1
                    stack.append(node)
print(count)
#실버2 / 40분 / 892ms

