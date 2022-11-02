def v_minus(v_b, i):
    v_a = v_b[:]
    v_a[i] -= 1
    return v_a 

def dfs(n, visited, last):
    global max_a, min_a
    if n == N:
        if last > max_a:
            max_a = last
        if last < min_a:
            min_a = last
        return
    for i in range(4):
        if i == 0 and visited[0] > 0:
            dfs(n+1, v_minus(visited, i), last + ARR[n])
        elif i == 1 and visited[1] > 0:
            dfs(n+1, v_minus(visited, i), last - ARR[n])
        elif i == 2 and visited[2] > 0:
            dfs(n+1, v_minus(visited, i), last * ARR[n])
        elif i == 3 and visited[3] > 0:
            if last < 0:
                dfs(n+1, v_minus(visited, i), -(abs(last) // ARR[n]))
            else: 
                dfs(n+1, v_minus(visited, i), last // ARR[n])

def sol(N, ARR, OPERATOR):
    global max_a, min_a
    max_a = -1000000000
    min_a = 1000000000
    dfs(1, OPERATOR[:], ARR[0])
    print(max_a)
    print(min_a)


N = int(input())
ARR = list(map(int, input().split()))
OPERATOR = list(map(int, input().split()))
sol(N, ARR, OPERATOR)

# 실버1 / 30분 / 128ms