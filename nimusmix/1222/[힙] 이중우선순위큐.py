import heapq

def solution(operations):
    min_h, max_h = [], []
    
    for operation in operations:
        operator, number = operation.split()
        number = int(number)
        if operator == 'I':
            heapq.heappush(min_h, number)
            heapq.heappush(max_h, -number)
        else:
            if len(min_h) == 0:
                pass
            elif number == 1:
                max_v = -heapq.heappop(max_h)
                min_h.remove(max_v)
            elif number == -1:
                min_v = heapq.heappop(min_h)
                max_h.remove(-min_v)
    return [0, 0] if not min_h else [-max_h[0], min_h[0]]


# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)