def subset(arr):
    n = len(arr)
    subsets = []
    for i in range(1 << n):
        subs = []
        for j in range(n):
            if i & (1 << j):  # j번 비트가 0이 아니면 arr[j]가 부분집합의 원소
                subs.append(arr[j])
        subsets.append(subs)
    return subsets


N = int(input())
P = []
for n in range(1, N + 1):
    t, p = map(int, input().split())
    P.append((n, t, p))

plans = subset(P)
max_val = 0
for plan in plans:
    days = len(plan)
    temp = 0
    for day in range(days):
        limit = plan[day][0] + plan[day][1] - 1
        if day != days - 1:
            if plan[day + 1][0] <= limit or N < limit:
                break
            else:
                temp += plan[day][2]
        else:
            if N < limit:
                break
            else:
                temp += plan[day][2]
    else:
        if max_val < temp:
            max_val = temp
print(max_val)
