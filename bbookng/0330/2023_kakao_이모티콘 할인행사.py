# 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것
# 2. 이모티콘 판매액을 최대한 늘리는 것

# n 명의 사용자들에게 이모티콘 m 개를 할인하여 판매, 10 ~ 40 %

# 1. 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매
# 2. 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입

def make_cases(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in make_cases(array, r-1):
                print(array[i], next)
                yield [array[i]] + next


def solution(users, emoticons):
    plus_members, sales_revenue = 0, 0
    cases = make_cases((10, 20, 30, 40), len(emoticons))

    for case in cases:
        plus, profit = 0, 0

        for std, limit in users:
            total = 0
            for i, sale_percent in enumerate(case):
                if sale_percent >= std:
                    total += emoticons[i] * (1 - sale_percent / 100)

            if total >= limit:
                plus += 1
            else:
                profit += int(total)

        plus_members, sales_revenue = max([plus_members, sales_revenue], [plus, profit])

    return [plus_members, sales_revenue]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.17ms, 10.3MB)
테스트 3 〉	통과 (0.62ms, 10.2MB)
테스트 4 〉	통과 (3.17ms, 10.2MB)
테스트 5 〉	통과 (6.47ms, 10.3MB)
테스트 6 〉	통과 (2.02ms, 10.2MB)
테스트 7 〉	통과 (18.07ms, 10.3MB)
테스트 8 〉	통과 (9.41ms, 10.2MB)
테스트 9 〉	통과 (115.15ms, 10.3MB)
테스트 10 〉	통과 (39.05ms, 10.2MB)
테스트 11 〉	통과 (419.66ms, 10.3MB)
테스트 12 〉	통과 (242.09ms, 10.2MB)
테스트 13 〉	통과 (1902.49ms, 10.3MB)
테스트 14 〉	통과 (1826.93ms, 10.1MB)
테스트 15 〉	통과 (122.98ms, 10.2MB)
테스트 16 〉	통과 (148.11ms, 10.2MB)
테스트 17 〉	통과 (0.41ms, 10.2MB)
테스트 18 〉	통과 (23.60ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10.2MB)
테스트 20 〉	통과 (0.11ms, 10.4MB)
'''