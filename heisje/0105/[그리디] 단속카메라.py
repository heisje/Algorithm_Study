# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    routes.sort()
    group = []
    group.append(routes[0])
    for i in range(1, len(routes)):
        for j in range(len(group)):
            # 교집합이 존재하면 누적하고 break
            if group[j][0] <= routes[i][0] <= group[j][1] or group[j][0] <= routes[i][1] <= group[j][1]:
                if group[j][0] < routes[i][0]:
                    group[j][0] = routes[i][0]
                if routes[i][1] < group[j][1]:
                    group[j][1] = routes[i][1]
                break
        # 교집합이 존재하지 않으면
        else:
            group.append(routes[i])
    return len(group)

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))


# 정확성  테스트
# 테스트 1 〉	통과 (0.07ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.2MB)
# 테스트 3 〉	통과 (0.15ms, 9.94MB)
# 테스트 4 〉	통과 (0.14ms, 10.2MB)
# 테스트 5 〉	통과 (0.15ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (10.53ms, 10.4MB)
# 테스트 2 〉	통과 (6.75ms, 10.2MB)
# 테스트 3 〉	통과 (28.77ms, 10.4MB)
# 테스트 4 〉	통과 (0.72ms, 10.1MB)
# 테스트 5 〉	통과 (37.69ms, 10.6MB)