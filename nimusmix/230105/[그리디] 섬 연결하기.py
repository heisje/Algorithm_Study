def solution(n, costs):
    def find_set(x):
        while x!= rep[x]:
            x = rep[x]
        return x

    def union(x, y):
        rep[find_set(y)] = find_set(x)
        
    costs.sort(key=lambda x:x[2])
    rep = [i for i in range(n)]
    cnt = total = 0
    
    for s, e, c in costs:
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            total += c
            
            if cnt == n-1:
                break
    
    return total


# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.06ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)