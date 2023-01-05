def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    cam = pointer = 0

    while pointer < len(routes):
        installed = routes[pointer][1]
        cam += 1
        pointer += 1
        while pointer < len(routes) and routes[pointer][0] <= installed <= routes[pointer][1]:
            pointer += 1
    return cam


# 정확성 테스트
# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)

# 효율성 테스트
# 테스트 1 〉	통과 (1.14ms, 10.5MB)
# 테스트 2 〉	통과 (0.77ms, 10.5MB)
# 테스트 3 〉	통과 (3.17ms, 10.6MB)
# 테스트 4 〉	통과 (0.13ms, 10.3MB)
# 테스트 5 〉	통과 (2.63ms, 10.8MB)
