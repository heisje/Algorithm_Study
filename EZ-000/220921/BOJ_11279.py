import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, -x)
    else:
        if heap:
            heap_max = heapq.heappop(heap)
            print(-heap_max)
        else:
            print(0)
