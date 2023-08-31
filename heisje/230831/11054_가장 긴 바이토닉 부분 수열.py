# 80ms
_ = input()
li = list(map(int, input().split()))

dp = [0 for _ in range(len(li))] 
up = [10000]
for i in range(len(li)):
    for u in range(len(up)):
        if li[i] <= up[u]:
            up[u] = li[i]
            break
    else:
        up.append(li[i])
    dp[i] += len(up)

up = [10000]
li.reverse()
for i in range(len(li)):
    for u in range(len(up)):
        if li[i] <= up[u]:
            up[u] = li[i]
            break
    else:
        up.append(li[i])
    dp[len(li)-1-i] += len(up)
    
print(max(dp)-1)
# 올라갈때, 내려갈때를 둘 다 체크해야함
# 10
# 1 5 2 1 4 3 4 5 2 1