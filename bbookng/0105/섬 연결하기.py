def find(p, n):
    if p[n] != n:
        p[n] = find(p, p[n])
    return p[n]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a > b:
        p[a] = b
    else:
        p[b] = a

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        land1, land2, fee = cost

        if find(parents, land1) != find(parents, land2):
            union(parents, land1, land2)
            answer += fee

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.11ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
'''