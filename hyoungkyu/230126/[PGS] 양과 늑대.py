from collections import deque

def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    res = []
    def dfs(s, w):
        if s > w:
            res.append(s)
        else:
            return 
        
        for n1, n2 in edges:
            if visited[n1] and not visited[n2]:
                visited[n2] = 1
                if info[n2] == 0:
                    dfs(s+1, w)
                else:
                    dfs(s, w+1)
                visited[n2] = 0
    dfs(1, 0)
    print(res)
    answer = max(res)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.13ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.39ms, 10.2MB)
테스트 6 〉	통과 (0.20ms, 10.1MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (0.37ms, 10MB)
테스트 10 〉	통과 (5.22ms, 10.1MB)
테스트 11 〉	통과 (0.12ms, 10.2MB)
테스트 12 〉	통과 (1.02ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.84ms, 10.2MB)
테스트 16 〉	통과 (1.26ms, 10.2MB)
테스트 17 〉	통과 (17.09ms, 10.3MB)
테스트 18 〉	통과 (0.33ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''