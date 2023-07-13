# 1152ms
import heapq

# 결과값으로 최단시간 반환
def sToE(start, end):
    hq = []
    visited = [float('inf') for _ in range(N+1)]
    visited[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        time, start = heapq.heappop(hq)
        if start == end:
            return time
        for goTime, next in node[start]:
            cost = goTime + time
            if cost < visited[next]:
                visited[next] = cost
                heapq.heappush(hq, (cost, next))

# N은 학생 수
# X는 마을 번호
# M은 단방향 도로 개수
N, M, X = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    START, END, TIME = map(int, input().split())   # Start, End, Time
    node[START].append((TIME, END))


# 집에서 x로 가는 거리 + x에서 집으로 가는 최단 거리의 합
answer = []
for n in range(1, N+1):
    if n != X:
        answer.append(sToE(n, X) + sToE(X, n))
print(max(answer))