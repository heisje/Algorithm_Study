from itertools import combinations

def solution(orders, course):
    answer = []

    for number in course:
        hash = dict()
        tmp = 0

        for order in orders:
            order = sorted(order)

            for com in combinations(order, number):
                combi = ''.join(com)
                if combi in hash:
                    hash[combi] += 1
                    tmp = max(hash[combi], tmp)
                else:
                    hash[combi] = 1

        if tmp > 1:
            for combi in hash:
                if hash[combi] == tmp:
                    answer.append(combi)

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

'''
테스트 1 〉	통과 (0.06ms, 10.1MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.11ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.4MB)
테스트 5 〉	통과 (0.10ms, 10.2MB)
테스트 6 〉	통과 (0.20ms, 10.4MB)
테스트 7 〉	통과 (0.29ms, 10.2MB)
테스트 8 〉	통과 (2.32ms, 10.4MB)
테스트 9 〉	통과 (1.15ms, 10.2MB)
테스트 10 〉	통과 (1.40ms, 10.4MB)
테스트 11 〉	통과 (0.63ms, 10.3MB)
테스트 12 〉	통과 (1.25ms, 10.4MB)
테스트 13 〉	통과 (1.30ms, 10.4MB)
테스트 14 〉	통과 (1.21ms, 10.3MB)
테스트 15 〉	통과 (1.04ms, 10.4MB)
테스트 16 〉	통과 (0.30ms, 10.4MB)
테스트 17 〉	통과 (0.16ms, 10.1MB)
테스트 18 〉	통과 (0.12ms, 10.4MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.25ms, 10.3MB)
'''