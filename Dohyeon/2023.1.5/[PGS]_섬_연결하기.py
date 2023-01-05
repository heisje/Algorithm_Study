def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


def solution(n, costs):
    parent = [0] * n
    for i in range(0, n):
        parent[i] = i
    costs.sort(key=lambda x:x[2])
    answer = 0
    for i in range(len(costs)):
        a, b, cost = costs[i][0], costs[i][1], costs[i][2]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.10ms, 10.1MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
"""