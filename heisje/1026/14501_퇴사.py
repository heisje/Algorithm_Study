def dfs(day, total):
    global max_total
    if day >= N:  
        if total > max_total:
            max_total = total
        return
    #print(day)
    if arr[day][0] != 0:
        dfs(day + arr[day][0], total + arr[day][1])
    dfs(day + 1, total)

N = int(input())
arr = [[0, 0] for _ in range(N)]
for n in range(N):
    due, money = map(int, input().split())
    if n+due <= N:
        arr[n] = [due, money]
max_total = 0
#print(arr)
dfs(0, 0)
print(max_total)

# 실버3 / 20분 / 86ms