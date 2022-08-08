N = int(input())
li = list(map(int, input().split()))

p = 1
m = 1
max_len = 1

for i in range(1, N):       
    if li[i-1] <= li[i]:
        p += 1
        max_len = p if p > max_len else max_len
    else:
        p = 1
        
    if li[i-1] >= li[i]:
        m += 1
        max_len = m if m > max_len else max_len
    else:
        m = 1
        
print(max_len)