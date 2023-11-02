from collections import deque

def solution(n, edge):
    visited = [0] * (n+1)
    nodes = [[] for _ in range(n+1)]
    
    for start, end in edge:
        nodes[start].append(end)
        nodes[end].append(start)
        
    dq = deque()
    dq.append((1, 0))
    visited[1] = 1
    answers = [0] * n
    answers_max = 0
    while dq:
        pre, dis = dq.popleft()
        
        for go in nodes[pre]:
            if visited[go] == 0:
                visited[go] = dis+1
                dq.append((go, dis+1))
                answers[dis+1] += 1
                answers_max = max(dis+1,answers_max)
    
    return answers[answers_max]