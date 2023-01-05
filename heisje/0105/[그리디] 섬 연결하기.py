# https://school.programmers.co.kr/learn/courses/30/lessons/42861
import heapq
def solution(n, costs):
    answer = 0
    visited = [0 for _ in range(n)]
    visited_len = 0
    nodes = [[] for _ in range(n)]
    
    # 노드연결
    for cost in costs:
        start, end, value = cost
        nodes[start].append((value, end))
        nodes[end].append((value, start))

    # 0에서 시작하기
    hq = []
    for node in nodes[0]:
        heapq.heappush(hq, node)
    visited[0] = 1

    # 우선순위큐로 다익스트라 
    while visited_len < n - 1:
        value, go = heapq.heappop(hq)
        if visited[go] == 0:
            visited[go] = 1
            visited_len += 1
            answer += value
            for node in nodes[go]:
                heapq.heappush(hq, node)

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.05ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)