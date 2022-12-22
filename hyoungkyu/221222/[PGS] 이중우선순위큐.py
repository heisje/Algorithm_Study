# Lv3 / Heap
import heapq

def remove_num(heap, num):
    for i in range(len(heap)):
        if heap[i][0] == num:
            heap.pop(i)
            return heap

def solution(operations):
    answer = [0, 0]
    min_heap = []
    max_heap = []
    for i in operations:
        oper, num = i.split()
        num = int(num)
        if oper == "I":
            heapq.heappush(min_heap, (num, -num))
            heapq.heappush(max_heap, (-num, num))
        elif oper == "D" and max_heap:
            if num == 1:
                maxV = heapq.heappop(max_heap)[1]
                min_heap = remove_num(min_heap, maxV)
            else:
                minV = heapq.heappop(min_heap)[1]
                max_heap = remove_num(max_heap, minV)
                
    print(f'min_heap = {min_heap}')
    print(f'max_heap = {max_heap}')
    if max_heap:
        answer = [max_heap[0][1], min_heap[0][0]]
    return answer

'''
테스트 1 〉 통과 (0.08ms, 10.4MB)   #
테스트 2 〉 통과 (0.03ms, 10.3MB)
테스트 3 〉 통과 (0.04ms, 10.3MB)
테스트 4 〉 통과 (0.02ms, 10.4MB)
테스트 5 〉 통과 (0.04ms, 10.3MB)
테스트 6 〉 통과 (0.04ms, 10.2MB)
'''