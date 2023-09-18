n, m, h = map(int, input().split())
visited = [[False] * (n+1) for _ in range(h+1)]
combi = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)
            visited[x][y] = False

for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)
# ----


# import sys
# input = sys.stdin.readline

# N, M, H = map(int, input().split())
# nodes = [[False]*(N) for _ in range(H)]

# #데이터 입력받기
# for _ in range(M):
#     h, n = map(int,input().split())
#     nodes[h-1][n-1] = True

# #현재 그래프 상태에서 조건을 만족하는지 판단.    
# def check():
#     for i in range(0, N-1):
#         start = i
#         for j in range(0, H):
#             #내려가던중 오른쪽으로 선있으면 숫자 +1
#             if nodes[j][start]:
#                 start += 1
#             #내려가던중 왼쪽에 선있으면 숫자 -1
#             elif nodes[j][start-1]:
#                 start -= 1
            
#         if start != i:
#             return False
#     return True

# result = 4
# #전체 탐색을 위한 재귀 함수
# def dfs(depth, x, y):
#     global result
#     if depth >= result :
#         return
    
#     #주어진 사다리가 조건을 충족하면 결과 갱신
#     if check():
#         result = min(result, depth)
#         return
    
#     if depth == 3:
#         return
  
#     #현재 깊이에서 안되면 다음 깊이 탐색                
#     for h in range(x, H):
#         ########################
#         if x == h:
#             k = y
#         else:
#             k = 0
#         ########################
#         for n in range(k, N-1):
#             if nodes[h][n] == False and nodes[h][n+1] == False and nodes[h][n-1] == False:
#                 nodes[h][n] = True
#                 #방금 추가해준 사다리 위치를 기억하고 그다음 사다리부터 추가되도록 작성
#                 #추가된 좌표를 하나의 값으로 바꿔서 다다음 함수로 보냄
#                 dfs(depth+1, h ,n+2)
#                 nodes[h][n] = False
                    
    
# dfs(0,0,0)
# if result == 4:
#     result = -1
    
# print(result)

# def check(cntt, nn, hh):
#     for i in range(N):
#         start = i
#         for h in range(H):
#             i += nodes[h][i]
#         if start != i:
#             print(cntt, nn, hh)
#             return False
#     print('성공', cntt, nn, hh)
#     return True

# def dfs(cnt, n, h):
#     global answer
#     if cnt > 3:
#         return
#     if check(cnt, n, h):
#         answer = min(answer, cnt)
#         return
#     if 0 <= n < N and 0 <= h < H:
#         return
    
#     if nodes[h][n] == 0 and nodes[h][n+1] == 0:
#         nodes[h][n] = 1
#         nodes[h][n+1] = -1
#         if h+1 >= H:
#             dfs(cnt + 1, n + 1, 0)
#         else:
#             dfs(cnt + 1, n, h + 1)
#         nodes[h][n] = 0
#         nodes[h][n+1] = 0
#     if h+1 >= H:
#         dfs(cnt, n + 1, 0)
#     else:
#         dfs(cnt, n, h + 1)
        

# N, M, H = map(int, input().split())
# nodes = [[0 for _ in range(N)] for _ in range(H)]
# answer = 100
# for _ in range(M):
#     a, b = map(int, input().split())
#     nodes[a-1][b-1] = 1
#     nodes[a-1][b] = -1

# dfs(0, 0, 0)
# if answer == 100:
#     print(-1)
# else:
#     print(answer)