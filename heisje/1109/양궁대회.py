# N:최대 화살개수, 
# n:지금까지 맞춘 화살 수, 
# target: 지금 맞추고있는 타겟
# INFO_A,b : a,b가 맞추고 있는 타겟
# score : 지금까지 총 점수
def dfs(N, n, target, INFO_A, info_b, score): 
    global max_score, save_info_b
    if n > N:
        return
    if target >= 10:
        # 결과계산
        if score != 0: # 0제외
            # 클 때 바꿔주기
            if max_score < score:
                max_score = score
                info_b[10] = N - sum(info_b[:10])
                save_info_b = [info_b[:]]
            # 같을 땐 append로 추가
            if max_score == score:
                info_b[10] = N - sum(info_b[:10])
                save_info_b.append(info_b[:])
        return
    # 이길 때
    info_b[target] = INFO_A[target]+1
    dfs(N, n+INFO_A[target]+1, target+1, INFO_A, info_b, score + (10-target))
    # 비길 때, 0일때만 비길 수 있었다니..
    if INFO_A[target] == 0:
        info_b[target] = 0
        dfs(N, n, target+1, INFO_A, info_b, score)
    # 질 때
    if INFO_A[target] > 0:
        info_b[target] = 0
        dfs(N, n, target+1, INFO_A, info_b, score - (10-target))

def solution(n, info):
    global max_score, save_info_b
    max_score = 0
    save_info_b = []
    dfs(n, 0, 0, info, [0]*11, 0)
    # 아니 이게 작은거 많이 맞추게 하는 법
    save_info_b.sort(key=lambda x:x[::-1])
    
    if save_info_b:
        return save_info_b[-1]  # 정렬해서 맨 뒤에꺼 
    else:
        return [-1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))

# LV.2 / 60분
# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.34ms, 10.3MB)
# 테스트 3 〉	통과 (0.42ms, 10.3MB)
# 테스트 4 〉	통과 (0.20ms, 10.2MB)
# 테스트 5 〉	통과 (0.37ms, 10.3MB)
# 테스트 6 〉	통과 (0.40ms, 10.4MB)
# 테스트 7 〉	통과 (0.21ms, 10.2MB)
# 테스트 8 〉	통과 (0.13ms, 10.2MB)
# 테스트 9 〉	통과 (0.19ms, 10.3MB)
# 테스트 10 〉	통과 (0.09ms, 10.3MB)
# 테스트 11 〉	통과 (0.16ms, 10.4MB)
# 테스트 12 〉	통과 (0.14ms, 10.2MB)
# 테스트 13 〉	통과 (0.51ms, 10.3MB)
# 테스트 14 〉	통과 (0.33ms, 10.2MB)
# 테스트 15 〉	통과 (0.38ms, 10.3MB)
# 테스트 16 〉	통과 (0.25ms, 10.4MB)
# 테스트 17 〉	통과 (0.23ms, 10.2MB)
# 테스트 18 〉	통과 (0.06ms, 10.4MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.75ms, 10.2MB)
# 테스트 21 〉	통과 (0.36ms, 10.3MB)
# 테스트 22 〉	통과 (0.43ms, 10.4MB)
# 테스트 23 〉	통과 (0.09ms, 10.2MB)
# 테스트 24 〉	통과 (0.45ms, 10.2MB)
# 테스트 25 〉	통과 (0.50ms, 10.3MB)