from pprint import pprint

# n은 노드 개수
# s: start

def solution(n, s, a, b, fares):
    graph = [[999999] * (n+1) for _ in range(n+1)]

    for n1, n2, cost in fares:
        graph[n1][n2] = cost
        graph[n2][n1] = cost

    for k in range(1, n+1):
        graph[k][k] = 0

    for m in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
                print(pprint(graph))

    answer = 9999999999
    for v in range(1, n+1):
        if answer > graph[s][v] + graph[v][a] + graph[v][b]:
            answer = graph[s][v] + graph[v][a] + graph[v][b]

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))

'''
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.38ms, 10.3MB)
테스트 5 〉	통과 (1.03ms, 10.3MB)
테스트 6 〉	통과 (0.81ms, 10.3MB)
테스트 7 〉	통과 (0.56ms, 10.3MB)
테스트 8 〉	통과 (1.36ms, 10.4MB)
테스트 9 〉	통과 (1.99ms, 10.3MB)
테스트 10 〉	통과 (2.53ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (296.27ms, 10.4MB)
테스트 2 〉	통과 (988.93ms, 11.1MB)
테스트 3 〉	통과 (2335.08ms, 11.3MB)
테스트 4 〉	통과 (2355.06ms, 11.4MB)
테스트 5 〉	통과 (2342.64ms, 11.4MB)
테스트 6 〉	통과 (2340.48ms, 11.4MB)
테스트 7 〉	통과 (2134.18ms, 13.7MB)
테스트 8 〉	통과 (2156.37ms, 14.1MB)
테스트 9 〉	통과 (2196.59ms, 13MB)
테스트 10 〉	통과 (2417.51ms, 13MB)
테스트 11 〉	통과 (2489.75ms, 12.8MB)
테스트 12 〉	통과 (2198.50ms, 12.7MB)
테스트 13 〉	통과 (2149.70ms, 12.6MB)
테스트 14 〉	통과 (2179.41ms, 12.7MB)
테스트 15 〉	통과 (2368.31ms, 12.8MB)
테스트 16 〉	통과 (2345.90ms, 11.5MB)
테스트 17 〉	통과 (2346.85ms, 11.2MB)
테스트 18 〉	통과 (2339.99ms, 11.3MB)
테스트 19 〉	통과 (2338.53ms, 11.4MB)
테스트 20 〉	통과 (2380.04ms, 11.7MB)
테스트 21 〉	통과 (2463.98ms, 11.8MB)
테스트 22 〉	통과 (2366.03ms, 12.8MB)
테스트 23 〉	통과 (2347.16ms, 12.8MB)
테스트 24 〉	통과 (2389.42ms, 12.7MB)
테스트 25 〉	통과 (2320.47ms, 11.2MB)
테스트 26 〉	통과 (2319.37ms, 10.9MB)
테스트 27 〉	통과 (2316.99ms, 10.6MB)
테스트 28 〉	통과 (2258.91ms, 10.4MB)
테스트 29 〉	통과 (294.20ms, 10.3MB)
테스트 30 〉	통과 (266.18ms, 10.4MB)
'''

