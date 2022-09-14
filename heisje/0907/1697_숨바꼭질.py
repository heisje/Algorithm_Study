#아이디어: 0~100001까지의 땅이 있으면, 수빈이가 초마다 어디까지 갈 수 있는지 visited에 전부 저장한다.
#          visited는 또한 다음 초에 갈 수 있는 위치를 모두 선택한다
from collections import deque
N, K = map(int, input().split())
if N > K:
    print(N-K)
    exit()
visited = [0]*100001 # 방문위치 (K-1의 두배해도 될 듯)
visited[N] = 1       # 수빈의 위치를 1로 지정 후 bfs로 구한다.
dq = deque()
dq.append(N)
while deque:         # bfs
    n = dq.popleft() # n은 수빈의 위치
    if n == K:       # 수빈이와 동생의 위치가 같아지면
        break
    elif n > K: # n > K, n이 K보다 크면 -1로만 움직인다. 
        if visited[n-1] == 0:
            dq.append(n-1)
            visited[n-1] = visited[n] + 1
    else:
        if 0 <= n-1 <= 100000 and visited[n-1] == 0: #뒤로 갈 경우 (인덱싱 에러방지) and (움직일 칸이 방문했는지)
            dq.append(n-1)
            visited[n-1] = visited[n] + 1
        if 0 <= n+1 <= 100000 and visited[n+1] == 0: #앞으로 갈 경우
            dq.append(n+1)
            visited[n+1] = visited[n] + 1
        if 0 <= n*2 <= 100000 and visited[n*2] == 0: #두배로 갈 경우 
            dq.append(n*2)
            visited[n*2] = visited[n] + 1
print(visited[K]-1)
    
#실버 1 / 160ms /20분

