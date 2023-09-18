from collections import deque
def solution(N, roads, sources, destination):
    answer = []
    locs = [0 for _ in range(N+1)]
    nodes = [[] for _ in range(N+1)]
    for a, b in roads:
        nodes[a].append(b)
        nodes[b].append(a)
        
    q = deque()
    q.append((destination, 0))  # 갈곳, depth
    visited = [-1 for _ in range(N+1)]
    visited[destination] = 0
    
    while q:
        pre, depth = q.popleft()
        
        for go in nodes[pre]:
            if visited[go] == -1:
                visited[go] = depth+1
                q.append((go, depth+1))

    for s in sources:
        answer.append(visited[s])
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.4MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (13.62ms, 16.1MB)
# 테스트 7 〉	통과 (15.62ms, 17.1MB)
# 테스트 8 〉	통과 (24.12ms, 22.1MB)
# 테스트 9 〉	통과 (7.30ms, 13.8MB)
# 테스트 10 〉	통과 (7.70ms, 14.5MB)
# 테스트 11 〉	통과 (504.27ms, 109MB)
# 테스트 12 〉	통과 (499.00ms, 110MB)
# 테스트 13 〉	통과 (615.38ms, 110MB)
# 테스트 14 〉	통과 (657.68ms, 110MB)
# 테스트 15 〉	통과 (686.21ms, 110MB)
# 테스트 16 〉	통과 (121.34ms, 39.3MB)