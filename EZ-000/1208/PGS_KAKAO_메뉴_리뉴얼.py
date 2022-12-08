from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course:
        choices = {}
        for order in orders:
            temp = combinations(sorted(list(order)), num)
            for comb in temp:
                if comb in choices.keys():
                    choices[comb] += 1
                else:
                    choices[comb] = 1
        max_cnt = max(choices.values(), default=0)
        if 1 < max_cnt:
            for key in choices:
                if choices[key] == max_cnt:
                    answer.append(''.join(key))
        answer.sort()
    return answer


# 테스트 1 〉	통과 (0.06ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.11ms, 10MB)
# 테스트 5 〉	통과 (0.08ms, 10.1MB)
# 테스트 6 〉	통과 (0.19ms, 10.3MB)
# 테스트 7 〉	통과 (0.22ms, 10.2MB)
# 테스트 8 〉	통과 (1.67ms, 10.1MB)
# 테스트 9 〉	통과 (1.17ms, 10.3MB)
# 테스트 10 〉 통과 (1.44ms, 10.4MB)
# 테스트 11 〉 통과 (1.25ms, 10.2MB)
# 테스트 12 〉 통과 (0.95ms, 10.4MB)
# 테스트 13 〉 통과 (1.26ms, 10.6MB)
# 테스트 14 〉 통과 (1.50ms, 10.3MB)
# 테스트 15 〉 통과 (1.28ms, 10.3MB)
# 테스트 16 〉 통과 (0.36ms, 10.1MB)
# 테스트 17 〉 통과 (0.20ms, 10.1MB)
# 테스트 18 〉 통과 (0.09ms, 10.2MB)
# 테스트 19 〉 통과 (0.03ms, 10.2MB)
# 테스트 20 〉 통과 (0.26ms, 10.2MB)
