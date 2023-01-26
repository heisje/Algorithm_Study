import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 플로이드-와샬
for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][k] == 1 or (graph[j][i] == 1 and graph[i][k] == 1):
                graph[j][k] = 1

for row in graph:
    for col in row:
        print(col, end=' ')
    print()

'''참고
https://claude-u.tistory.com/336
'''