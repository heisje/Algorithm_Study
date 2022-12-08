from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = defaultdict(int)
    for order in orders:
        for i in range(len(course)):
            for j in combinations(order, course[i]):
                j = list(j)
                j.sort()
                tmp = "".join(j)
                dic[tmp] += 1
                
    tmp = [[] for _ in range(len(course))]
    for pick, num in dic.items():
        if num >= 2:
            if tmp[course.index(len(pick))]:
                if num == tmp[course.index(len(pick))][0][1]:
                    tmp[course.index(len(pick))].append([pick, num])
                elif num > tmp[course.index(len(pick))][0][1]:
                    tmp[course.index(len(pick))] = [[pick, num]]
                else:
                    pass
            else:
                tmp[course.index(len(pick))] = [[pick, num]]

    for i in tmp:
        for j in i:
            answer.append(j[0])
    answer.sort()
    return answer

'''
테스트 1 〉통과 (0.10ms, 10.2MB)
테스트 2 〉통과 (0.06ms, 10.3MB)
테스트 3 〉통과 (0.11ms, 10.3MB)
테스트 4 〉통과 (0.11ms, 10.3MB)
테스트 5 〉통과 (0.10ms, 10.3MB)
테스트 6 〉통과 (0.29ms, 10.3MB)
테스트 7 〉통과 (0.35ms, 10.3MB)
테스트 8 〉통과 (2.91ms, 10.3MB)
테스트 9 〉통과 (1.93ms, 10.4MB)
테스트 10 〉통과 (2.29ms, 10.7MB)
테스트 11 〉통과 (1.23ms, 10.3MB)
테스트 12 〉통과 (1.47ms, 10.4MB)
테스트 13 〉통과 (2.37ms, 10.5MB)
테스트 14 〉통과 (1.43ms, 10.5MB)
테스트 15 〉통과 (2.11ms, 10.6MB)
테스트 16 〉통과 (0.55ms, 10.3MB)
테스트 17 〉통과 (0.31ms, 10.4MB)
테스트 18 〉통과 (0.12ms, 10.3MB)
테스트 19 〉통과 (0.03ms, 10.3MB)
테스트 20 〉통과 (0.43ms, 10.4MB)
'''