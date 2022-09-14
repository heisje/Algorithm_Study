import heapq
from heapq import heappop
from heapq import heappush
import sys
input = sys.stdin.readline

testcase = int(input())
for tc in range(testcase):
    N = int(input())

    heap = []


    for i in range(N):
        order, a = input().split()
        num = int(a)

        if order == "I":
            heappush(heap, num)

        else:
            if not heap:  # 삭제할 데이터가 없다면
                continue
            if num == -1:
                heappop(heap)
            else:
                heap.remove(heapq.nlargest(1, heap)[0])

    if len(heap) == 0:
        print("EMPTY")
    else:
        print(heapq.nlargest(1, heap)[0], heappop(heap))

