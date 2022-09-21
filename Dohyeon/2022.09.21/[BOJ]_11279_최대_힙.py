import heapq
import sys
from heapq import heappop

input = lambda: sys.stdin.readline().strip()

heap = []

N = int(input())

for line in range(N):
    num = int(input())

    if num == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
            continue

    else:
        heapq.heappush(heap, (-num, num))
