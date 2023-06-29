# 골드3 / 76ms
import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
adjL1 = [[] for _ in range(N+1)]        # X로 갈 때
adjL2 = [[] for _ in range(N+1)]        # 집으로 갈 때

for _ in range(M):
    s, e, t = map(int, input().split())
    adjL1[e].append((t, s))
    adjL2[s].append((t, e))

def Dijkstra(X, adjL):
    visited = [float('inf')] * (N+1)
    visited[X] = 0
    queue = []
    heapq.heappush(queue, (0, X))
    while queue:
        time, idx = heapq.heappop(queue)
        if visited[idx] < time:
            continue
        for t, i in adjL[idx]:
            if visited[i] > time + t:
                visited[i] = time + t
                heapq.heappush(queue, (time+t, i))
    return visited

visited1 = Dijkstra(X, adjL1)
visited2 = Dijkstra(X, adjL2)
answer = 0
for i in range(1, N+1):
    answer = max(answer, visited1[i]+visited2[i])
print(answer)