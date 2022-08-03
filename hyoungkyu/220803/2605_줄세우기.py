N = int(input())
n = list(map(int,input().split()))
l = []
for i in range(0, N):
    l.insert(i - n[i],i+1)
for i in l:
    print(i, end=' ')