import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

answer = 0

def solution(num):
    distance = [float('inf')] * (N+1)
    distance[num] = 0

    q = []
    heapq.heappush(q, (0, num))

    while q:
        d, x = heapq.heappop(q)
        if distance[x] >= d:
            for e, t in graph[x]:
                if d + t < distance[e]:
                    distance[e] = d + t
                    heapq.heappush(q, (d + t, e))

    return distance

for i in range(1, N+1):
    if i == X:
        continue
    else:
        go = solution(i)[X]
        back = solution(X)[i]
        answer = max(answer, (go + back))

print(answer)




