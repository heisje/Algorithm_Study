import heapq
import sys
input = lambda: sys.stdin.readline().strip()

T = int(input())

for _ in range(T):
    k = int(input())
    heap = []
    max_heap = []
    for _ in range(k):
        c, d = input().split()
        d = int(d)
        
        if c == 'I':
            heapq.heappush(heap, d)
            heapq.heappush(max_heap, -d)
        elif d == 1:
            if heap:
                maxV = heapq.heappop(max_heap)
                heap.remove(-maxV)
        elif d == -1:
            if heap: 
                minV = heapq.heappop(heap)
                max_heap.remove(-minV)
    
    if not heap: print('EMPTY')
    else: print(max_heap[0], heap[0])