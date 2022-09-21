import sys
import heapq
input = lambda :sys.stdin.readline().strip()

N = int(input())
heap = []

for i in range(N):
    X = int(input())
    if X == 0:
        print(-heapq.heappop(heap)) if heap else print(0)
    else:
        heapq.heappush(heap, -X)

