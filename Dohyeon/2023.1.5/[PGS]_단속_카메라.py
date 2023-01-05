def solution(routes):
    answer = 0
    camera = []
    routes.sort(key=lambda x:x[1])
    for i in range(len(routes)):
        check = False
        for j in range(len(camera)):
            if camera[j] > routes[i][1]:
                break
            if routes[i][0] <= camera[j] <= routes[i][1]:
                check = True
                break
        if check:
            continue
        else:
            camera.append(routes[i][1])
            answer += 1
    return answer

"""
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.11ms, 10.1MB)
테스트 3 〉	통과 (0.14ms, 10MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (6.26ms, 10.5MB)
테스트 2 〉	통과 (3.45ms, 10.3MB)
테스트 3 〉	통과 (15.30ms, 10.6MB)
테스트 4 〉	통과 (0.46ms, 10.3MB)
테스트 5 〉	통과 (19.63ms, 10.7MB)
"""