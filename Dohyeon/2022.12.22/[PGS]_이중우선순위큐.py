import heapq
from heapq import heappop
from heapq import heappush

def solution(operations):
    heap = []
    for i in range(len(operations)):
        order, a = operations[i].split()
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

    if not heap:
        return [0, 0]
    else:
        return [heapq.nlargest(1, heap)[0],heap[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

"""
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(min_heap, int(i[1:]))
            heapq.heappush(max_heap, (-int(i[1:]), int(i[1:])))
        elif len(min_heap) == 0:
            continue
        elif int(i[1:]) == 1:
            heapq.heappop(max_heap)
            min_heap.pop()
        else:
            heapq.heappop(min_heap)
            max_heap.pop()
    if len(min_heap) > 0:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]
        
출처 : https://school.programmers.co.kr/questions/24607
"""

"""
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (3.08ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
"""