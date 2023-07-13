# 골드4
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
adjL = [{} for _ in range(V+1)]
K = int(input())                    # 시작 정점
for _ in range(E):
    u, v, w = map(int, input().split())
    if v not in adjL[u]:
        adjL[u][v] = 11
    adjL[u][v] = min(w, adjL[u][v])

def Dijkstra(V, K):
    visited = [float('INF')] * (V+1)
    visited[K] = 0
    queue = []
    heapq.heappush(queue, (0, K))
    while queue:
        distance, idx = heapq.heappop(queue)
        if visited[idx] < distance:
            continue
        for i in adjL[idx].keys():
            w = adjL[idx][i]
            if w + distance < visited[i]:
                visited[i] = w + distance
                heapq.heappush(queue, (w + distance, i))
    for i in range(1, V+1):
        if visited[i] == float('inf'):
            print('INF')
        else:
            print(visited[i])

Dijkstra(V, K)
