# 골드4 / 8116ms
import sys, heapq
input = lambda :sys.stdin.readline().strip()

for _ in range(int(input())):
    K = int(input())
    max_heap = []
    min_heap = []
    visited = [0] * (K+1)
    for i in range(1, K+1):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(max_heap, (-b, i))
            heapq.heappush(min_heap, (b, i))
        else:
            if b == 1:
                while max_heap and visited[max_heap[0][1]] != 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 1
                    heapq.heappop(max_heap)
            else:
                while min_heap and visited[min_heap[0][1]] != 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 1
                    heapq.heappop(min_heap)

    while max_heap and visited[max_heap[0][1]] != 0:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] != 0:
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])