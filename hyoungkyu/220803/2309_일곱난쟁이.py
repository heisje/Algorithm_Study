hap = []
l = []
for i in range(9):
    n = int(input())
    hap.append(n)
hap.sort()
su = sum(hap)

for i in range(0,9):  
    for j in range(i+1,9):
        if su - hap[i] - hap[j] == 100:
            l = [hap[i], hap[j]]
            break
hap.remove(l[0])
hap.remove(l[1])
for i in hap:
    print(i)