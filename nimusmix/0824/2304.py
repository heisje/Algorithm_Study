import sys
input = sys.stdin.readline

N = int(input())

li = []

for i in range(N):
    li.append(tuple((map(int, input().split()))))
    
li.sort()

s_idx = li[0]
e_idx = li[-1]
h_idx = max(li, key=lambda a:a[1])

max_area = (e_idx[0]+1 - s_idx[0]) * h_idx[1]
small_area = 0

standard = s_idx
for i in range(1, li.index(h_idx)+1):
    if li[i][1] > standard[1]:
        small_area += (li[i][0] - standard[0]) * (h_idx[1] - standard[1])
        standard = li[i]

standard = e_idx
for i in range(N-2, li.index(h_idx)-1, -1):
    if li[i][1] > standard[1]:
        small_area += (standard[0] - li[i][0]) * (h_idx[1] - standard[1])
        standard = li[i]

print(max_area - small_area)