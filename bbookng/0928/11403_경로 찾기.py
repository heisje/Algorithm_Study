import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):                                              # k를 중간 거치는 점이라 치고
    for i in range(N):                                          # 전체 graph 를 돌면서
        for j in range(N):                                      # i 에서 시작해서 k 로 이어져 j로 가는길이 있다면
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1                                 # 1로 변경

for i in graph:
    print(*i)



