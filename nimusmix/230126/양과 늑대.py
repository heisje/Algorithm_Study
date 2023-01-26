def solution(info, edges):
    ans = []
    visited = [0] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            ans.append(sheep)
        else:
            return
            
        for s, e in edges:
            if visited[s] and not visited[e]:
                visited[e] = 1
                if info[e] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[e] = 0
    
    visited[0] = 1
    dfs(1, 0)
    
    return max(ans)


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.12ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.36ms, 10.3MB)
# 테스트 6 〉	통과 (1.19ms, 10.1MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.1MB)
# 테스트 9 〉	통과 (0.35ms, 9.99MB)
# 테스트 10 〉	통과 (5.71ms, 10.2MB)
# 테스트 11 〉	통과 (0.19ms, 10MB)
# 테스트 12 〉	통과 (1.81ms, 10.1MB)
# 테스트 13 〉	통과 (0.04ms, 10.1MB)
# 테스트 14 〉	통과 (0.11ms, 10MB)
# 테스트 15 〉	통과 (0.40ms, 10.1MB)
# 테스트 16 〉	통과 (1.01ms, 10.2MB)
# 테스트 17 〉	통과 (14.81ms, 10.1MB)
# 테스트 18 〉	통과 (0.53ms, 10.2MB)