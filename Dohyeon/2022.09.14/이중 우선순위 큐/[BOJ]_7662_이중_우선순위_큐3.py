import heapq
import sys
input = sys.stdin.readline


def solution(n):
    heap = []

    for i in range(n):
        command, a = input().split()
        num = int(a)

        if command == 'D':
            if not heap:  # 삭제할 데이터가 없다면
                continue
            if num == '1':  # 최댓값 삭제
                heap.remove(heapq.nlargest(1, heap)[0])
            else:  # 최솟값 삭제
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, int(num))

    return [heapq.nlargest(1, heap)[0], heap[0]] if heap else [0, 0]



testcase = int(input())
for tc in range(testcase):
    N = int(input())
    print(solution(N))
