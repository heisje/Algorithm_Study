from itertools import combinations
from collections import defaultdict


# 문제풀이
def solution(orders, course):
    answer = []
    
    # 코스별 숫자대로 찾는데,
    for number in course:
        number_dict = defaultdict(int) # 여기에 개수대로 찾을 것임.
        max_count = 0

        # 오더에 따라 코스 갯수 대로 찾을 것임.
        for order in orders:

            # 코스의 개수에 따른 모든 조합을 찾는다. 근데, 메뉴를 솔트 한 번 해주고
            for combi in combinations(sorted(list(order)), number):
                number_dict[combi] += 1

                # 최대값 갱신
                if max_count < number_dict[combi]:
                    max_count = number_dict[combi]

        # 2개 이상, maxcount찾아서 문자열로 반환
        for key, value in number_dict.items():
            if value == max_count and value >= 2:
                answer.append(''.join(key))
    
    # 정리
    answer.sort()
    return answer


a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
b = [2,3,4]
print(solution(a,b))
a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
b = [2,3,5]
print(solution(a,b))
a = ["XYZ", "XWY", "WXA"]
b = [2,3,4] 
print(solution(a,b))


# 테스트 1 〉	통과 (0.07ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.1MB)
# 테스트 3 〉	통과 (0.07ms, 10.1MB)
# 테스트 4 〉	통과 (0.08ms, 10.1MB)
# 테스트 5 〉	통과 (0.08ms, 10.1MB)
# 테스트 6 〉	통과 (0.19ms, 10.1MB)
# 테스트 7 〉	통과 (0.21ms, 10.3MB)
# 테스트 8 〉	통과 (3.06ms, 10.4MB)
# 테스트 9 〉	통과 (1.24ms, 10.2MB)
# 테스트 10 〉	통과 (1.59ms, 10.3MB)
# 테스트 11 〉	통과 (0.94ms, 10.4MB)
# 테스트 12 〉	통과 (1.25ms, 10.2MB)
# 테스트 13 〉	통과 (1.55ms, 10.6MB)
# 테스트 14 〉	통과 (1.22ms, 10.5MB)
# 테스트 15 〉	통과 (1.52ms, 10.5MB)
# 테스트 16 〉	통과 (0.69ms, 10.1MB)
# 테스트 17 〉	통과 (0.23ms, 10.2MB)
# 테스트 18 〉	통과 (0.10ms, 10.1MB)
# 테스트 19 〉	통과 (0.03ms, 10.2MB)
# 테스트 20 〉	통과 (0.27ms, 10.2MB)