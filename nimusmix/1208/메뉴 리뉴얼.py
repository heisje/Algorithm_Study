from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    ans = []
    all_combis = {}

    for num in course:
        all_combis[num] = defaultdict(int)

    for order in orders:
        for num in course:
            for combi in combinations(order, num):
                all_combis[num][tuple(sorted(combi))] += 1

    for num in all_combis:
        if not all_combis[num]:
            continue
        
        max_cnt = max(all_combis[num].values())
        if max_cnt < 2:
            continue

        for key, value in all_combis[num].items():
            if value == max_cnt:
                ans.append(''.join(key))

    ans.sort()
    return ans


# 테스트 1 〉	통과 (0.09ms, 10.3MB)
# 테스트 2 〉	통과 (0.10ms, 10.4MB)
# 테스트 3 〉	통과 (0.10ms, 10.1MB)
# 테스트 4 〉	통과 (0.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.09ms, 10.3MB)
# 테스트 6 〉	통과 (0.31ms, 10.3MB)
# 테스트 7 〉	통과 (0.26ms, 10.2MB)
# 테스트 8 〉	통과 (2.74ms, 10.3MB)
# 테스트 9 〉	통과 (1.84ms, 10.4MB)
# 테스트 10 〉	통과 (4.44ms, 10.7MB)
# 테스트 11 〉	통과 (1.27ms, 10.4MB)
# 테스트 12 〉	통과 (1.60ms, 10.4MB)
# 테스트 13 〉	통과 (2.22ms, 10.4MB)
# 테스트 14 〉	통과 (1.67ms, 10.5MB)
# 테스트 15 〉	통과 (2.32ms, 10.5MB)
# 테스트 16 〉	통과 (0.61ms, 10.4MB)
# 테스트 17 〉	통과 (0.35ms, 10.3MB)
# 테스트 18 〉	통과 (0.13ms, 10.4MB)
# 테스트 19 〉	통과 (0.02ms, 10.2MB)
# 테스트 20 〉	통과 (0.41ms, 10.2MB)