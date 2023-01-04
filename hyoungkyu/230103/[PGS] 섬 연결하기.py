# Lv3
def solution(n, costs):
    answer = 0
    adjM = [[0]*(n+1) for _ in range(n+1)]
    for cost in costs:
        adjM[cost[0]][cost[1]] = cost[2]
        adjM[cost[1]][cost[0]] = cost[2]

    def prim(r, V):
        MST = [0] * (V)
        MST[r] = 1
        s = 0
        for _ in range(V-1):
            u = 0
            minV = float('inf')
            for i in range(V):
                if MST[i] == 1:
                    for j in range(V):
                        if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                            u = j
                            minV = adjM[i][j]
            s += minV
            MST[u] = 1
        return s
        
    answer = prim(0, n)
                
    return answer

'''
테스트 1 〉 통과 (0.02ms, 10.3MB)
테스트 2 〉 통과 (0.03ms, 10.3MB)
테스트 3 〉 통과 (0.08ms, 10.2MB)
테스트 4 〉 통과 (0.23ms, 10MB)
테스트 5 〉 통과 (0.06ms, 10.1MB)
테스트 6 〉 통과 (0.29ms, 10.3MB)
테스트 7 〉 통과 (0.24ms, 10.1MB)
테스트 8 〉 통과 (0.07ms, 10.4MB)
'''