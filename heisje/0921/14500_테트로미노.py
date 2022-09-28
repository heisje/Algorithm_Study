import sys
lambda input : sys.stdin.readline()


delta = ((0,1), (0,-1), (1,0), (-1,0))


def tetrees(count, plus, x, y, visited): # 부르트포스로 싹 다 구하기
    if count == 4:
        result.append(plus)
        return
    
    for dx, dy in delta:
        
        if 0 <= y+dy < N and 0 <= x+dx < M:
            if not visited[y+dy][x+dx]:
                visited[y+dy][x+dx] = (x, y)
                tetrees(count + 1, plus + arr[y+dy][x+dx], x+dx, y+dy, visited)
                visited[y+dy][x+dx] = 0
        

def cjf(x, y): # ㅗ 모양만 찾는 함수
    a = []
    for dx, dy in delta: #상하좌우다 더하기
        if 0 <= y+dy < N and 0 <= x+dx < M:
            a.append(arr[y+dy][x+dx])
    if len(a) == 3: #세개면 그냥
        result.append(arr[y][x] + sum(a))
    else: #네개면 하나씩 뺀게 정답
        sum_a = sum(a)
        temp = []
        for b in a:
            temp.append(sum_a - b)
        result.append(max(temp)+arr[y][x])
    return




N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
base_visited = [[0] * M for _ in range(N)]
result = []
for y in range(N):
    for x in range(M):
        tetrees(0, 0, x, y, base_visited)
        cjf(x, y)
    
print(max(result))

