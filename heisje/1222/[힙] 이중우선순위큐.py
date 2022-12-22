# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# 이중 우선 순위 큐 푸는 법
# 메인 아이디어 : 딕셔너리를 이용해서 값이 존재하는지 안하는지 파악하고, 
# 최소힙, 최대힙 두가지를 만들어서 연산하면서 이미 다른 힙에서 사라진 값이면 계속해서 뺀다.
import heapq
from collections import defaultdict
def solution(operations):
    answer = [0, 0]

    dic = defaultdict(int)
    max_hp = []
    min_hp = []
    for op in operations:
        if op[0] == "I":
            num = int(op[2:])
            dic[num] += 1
            heapq.heappush(max_hp, -num)
            heapq.heappush(min_hp, num)
        elif op == "D 1":
            # 하나를 추출해봤는데
            if max_hp:
                num = -heapq.heappop(max_hp)
                # 비어있으면, 또 추출한다.
                while dic[num] == 0:
                    if max_hp:
                        num = -heapq.heappop(max_hp)
                    else:
                        break
                dic[num] -= 1
        elif op == "D -1":
            if min_hp:
                num = heapq.heappop(min_hp)
                # 비어있으면, 또 추출한다.
                while dic[num] == 0:
                    if min_hp:
                        num = heapq.heappop(min_hp)
                    else:
                        break
                dic[num] -= 1
    
    if max_hp:
        num = -heapq.heappop(max_hp)
        # 비어있으면, 또 추출한다.
        while dic[num] == 0:
            if max_hp:
                num = -heapq.heappop(max_hp)
            else:
                break
        if dic[num] != 0:
            answer[0] = num
    if min_hp:
        num = heapq.heappop(min_hp)
        # 비어있으면, 또 추출한다.
        while dic[num] == 0:
            if min_hp:
                num = heapq.heappop(min_hp)
            else:
                break
        
        if dic[num] != 0:
            answer[1] = num

    return answer


a = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(a))
a = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	
print(solution(a))


# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.07ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.04ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)