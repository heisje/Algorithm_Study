from collections import deque

R, C = map(int, input().split())
cheese = list(list(map(int, input().split())) for _ in range(R))
# cnt = 0
# for r in range(R):
#     for c in range(C):
#         if cheese[r][c] == 1:
#             cnt += 1
visited = [[0 for _ in range(C)] for _ in range(R)]
visited [0][0] = 1

hour = 0
dq = [deque(), deque()]
dq[hour].append((0, 0))
cnt = [0, 0]
# 0,0 부터 반복한다.
# 1 만나면 -1로 전부 바꾼다. dq에 저장해둔다. 
# 더 바꿀 수 있는 것이 없으면 dq를 전환한다.
# dq의 갯수를 세어놓는다.
while True:
    r, c = dq[hour].popleft()
    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        
        gr = r + dr
        gc = c + dc
        
        if 0 <= gr < R and 0 <= gc < C and visited[gr][gc] == 0:
            if cheese[gr][gc] == 0 :
                visited[gr][gc] = 1
                dq[hour].append((gr, gc))
            if cheese[gr][gc] == 1 :
                dq[hour + 1].append((gr, gc))
                cheese[gr][gc] = 2
                visited[gr][gc] = 1
                cnt[hour] += 1
    
    # 현재 찾는 것이 비어있으면 
    if not dq[hour]:
        # 다음 것도 비어있으면
        if not dq[hour+1]:
            break
        else:
            cnt.append(0)
            hour+=1
            dq.append(deque())

print(hour)
print(cnt[-3])