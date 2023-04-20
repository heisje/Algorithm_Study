def rotation(rows, columns, arr, query):
    D = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 시계 방향
    i1, j1, i2, j2 = query
    tmp = arr[i1-1][j1-1]                   # 바꿔줄 변수
    min_Value = tmp                         # 최소값
    visited = [[0] * columns for _ in range(rows)]
    visited[i1-1][j1-1] = 1                 # 초기 위치 체크
    idx = 0                                 # 방향
    ci, cj = i1-1, j1-1                     # 현재 위치
    
    while True:
        ni, nj = ci + D[idx][0], cj + D[idx][1] # 다음 위치
        if i1-1 > ni or i2-1 < ni or j1-1 > nj or j2-1 < nj:    # 다음 위치가 범위 안이 아니면 방향 바꿈
            idx += 1
            continue
            
        if visited[ni][nj]:                 # 한바퀴 다 돌면 끝
            break
            
        visited[ni][nj] = 1                 # 방문 체크
        tmp, arr[ni][nj] = arr[ni][nj], tmp # 값 바꾸기
        min_Value = min(min_Value, tmp)     # 최소값 갱신
        ci, cj = ni, nj                     # 다음 위치로 이동
        
    arr[i1-1][j1-1] = tmp                   # 초기 위치에 마지막 값 할당
    
    return min_Value
            

def solution(rows, columns, queries):
    answer = []
    arr = [[j for j in range(1 + i * columns, i * columns + columns + 1)] for i in range(rows)]
    for query in queries:
        answer.append(rotation(rows, columns, arr, query))
    return answer

'''

테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
    테스트 3 〉	통과 (575.63ms, 11.7MB)
테스트 4 〉	통과 (276.76ms, 11.2MB)
테스트 5 〉	통과 (535.60ms, 11.5MB)
테스트 6 〉	통과 (457.82ms, 11.8MB)
테스트 7 〉	통과 (509.01ms, 12MB)
테스트 8 〉	통과 (300.20ms, 11.1MB)
테스트 9 〉	통과 (414.79ms, 11.6MB)
테스트 10 〉	통과 (367.17ms, 11.4MB)
테스트 11 〉	통과 (318.33ms, 11.4MB)
'''