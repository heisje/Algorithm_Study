N = int(input())
plan = []
for i in range(N):
    plan.append(list(map(int, input().split())))

data_base = [0] * (N + 1)

def counting(income, today):

    if today == N:
        if data_base[today] < income:
            data_base[today] = income
        return
    if data_base[today] <= income:
        data_base[today] = income
    else:
        return
    counting(income, today + 1)
    if today + plan[today][0] > N:
        return
    counting(income + plan[today][1], today + plan[today][0])

counting(0, 0)

print(data_base[-1])