N = int(input())
all_li = []

for i in range(N//2+1):
    li = [N]
    li.append(N-i)
    for jdx, j in enumerate(li):
        try:
            if j-li[jdx+1] >= 0:
                li.append(j-li[jdx+1])
        except:
            pass
    all_li.append(li)
    
max_len = 2
len_li = []
    
for kdx, k in enumerate(all_li):
    if len(k) > max_len:
        max_len = len(k)
        len_li.append(kdx)

print(len(all_li[len_li[-1]]))
print(*all_li[len_li[-1]])