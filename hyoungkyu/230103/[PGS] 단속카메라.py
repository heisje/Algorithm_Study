# Lv3
def solution(routes):
    answer = -1
    routes.sort()
    end = float('-inf')
    flag = False
    for i in range(len(routes)):
        flag = True
        if end < routes[i][0]:
            answer += 1
            end = routes[i][1]
            flag = False
            if i == len(routes)-1:
                flag = True
        else:
            if end > routes[i][1]:
                end = routes[i][1]
    if flag:
        answer += 1
    return answer

'''
정확성 테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.08ms, 9.99MB)
테스트 3 〉	통과 (0.05ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (1.58ms, 10.2MB)
테스트 2 〉	통과 (1.01ms, 10.3MB)
테스트 3 〉	통과 (3.03ms, 10.6MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (3.29ms, 10.8MB)
'''