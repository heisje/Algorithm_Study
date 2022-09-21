import heapq
import sys
N = int(input())

a = []
for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0:
        if a:
            print(heapq.heappop(a)*-1)
        else:
            print(0)
    else:
        heapq.heappush(a, -value)

#실버2 / 3분 / 156ms