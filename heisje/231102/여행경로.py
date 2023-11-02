from collections import defaultdict
from copy import deepcopy
def solution(tickets):
    nodes = defaultdict(list)
    ticket_idx = 0
    for s, e in tickets:
        nodes[s].append((e, ticket_idx))
        ticket_idx += 1
    
    for node in nodes:
        nodes[node].sort()
        
    answer = []
    
    def loop(pre, answer, visited):
        if len(answer) == len(tickets)+1:
            save_answer[0] = answer[:]
            return answer
        for go, idx in ns[pre]:
            if idx not in visited:
                visited.add(idx)
                if loop(go, answer+[go], visited):
                    return answer
                visited.remove(idx)
                
    save_answer = [[]]
    answer = ["ICN"]
    st = [("ICN", answer)]
    ns = deepcopy(nodes)
    vis = set()
    save_answer = [[]]
    loop("ICN", answer, vis)
    if save_answer[0]:
        return save_answer[0]
    return 0

# 테스트 1 〉	통과 (0.16ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.4MB)