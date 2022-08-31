# 68ms / 실버1
import sys
input = lambda : sys.stdin.readline().strip()

def BFS(dic, S):                                    # dic : 경로, S : 첫 위치
    cnt = 0
    visited = [-1] * (N+1)                          # 방문 체크리스트
    visited[S] = 0
    queue = dic[S][:]                               # 얕은 복사를 안하면 queue를 팝할 때 dic의 값이 바뀜ㄷㄷ
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            t = queue.pop(0)
            visited[t] = cnt                        # 방문 리스트에 바로 이동거리 입력
            for s in dic[t]:                        # 이동한 위치에서 이동가능한 경로를 queue에 추가
                if visited[s] == -1 and s not in queue:
                    queue.append(s)
    return sum(visited)

N, M = map(int, input().split())
dic = {i:[] for i in range(1, N+1)}
for _ in range(M):                                  # 경로 만들기
    a, b = map(int, input().split())
    if b not in dic[a]:
        dic[a].append(b)
    if a not in dic[b]:
        dic[b].append(a)
stack = []                                          # stack에 각 점의 케빈베이컨 수를 입력
for i in range(1, N+1):
    stack.append(BFS(dic, i)+1)
print(stack.index(min(stack))+1)                    # 출력
