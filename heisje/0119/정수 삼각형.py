#https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    visited = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    visited[0][0] = triangle[0][0]

    for idx, tri in enumerate(triangle):
        if idx != 0:
            for jdx, t in enumerate(tri):
                # 앞에꺼와 뒤에 것중 큰것
                # print(idx, jdx)
                if 0 < jdx < len(tri)-1:
                    if visited[idx-1][jdx-1] < visited[idx-1][jdx]:
                        visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx]
                    else:
                        visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx-1]
                elif jdx == 0:
                    visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx]
                elif jdx == len(tri)-1:
                    visited[idx][jdx] = triangle[idx][jdx] + visited[idx-1][jdx-1]

    # print(visited)
    return max(visited[-1])

tr = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tr))


# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10MB)
# 테스트 2 〉	통과 (0.03ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.19ms, 10.1MB)
# 테스트 5 〉	통과 (1.30ms, 10.4MB)
# 테스트 6 〉	통과 (0.41ms, 10.3MB)
# 테스트 7 〉	통과 (1.44ms, 10.3MB)
# 테스트 8 〉	통과 (0.30ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.18ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (45.93ms, 18MB)
# 테스트 2 〉	통과 (35.63ms, 16.1MB)
# 테스트 3 〉	통과 (52.91ms, 19MB)
# 테스트 4 〉	통과 (47.00ms, 18MB)
# 테스트 5 〉	통과 (44.62ms, 17.4MB)
# 테스트 6 〉	통과 (54.24ms, 19.2MB)
# 테스트 7 〉	통과 (46.00ms, 18.7MB)
# 테스트 8 〉	통과 (43.20ms, 17.1MB)
# 테스트 9 〉	통과 (40.40ms, 17.4MB)
# 테스트 10 〉	통과 (51.64ms, 18.7MB)