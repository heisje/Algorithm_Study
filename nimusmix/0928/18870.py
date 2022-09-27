import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
li = list(map(int, input().split()))
li2 = sorted(set(li))
dict = {}

for idx, i in enumerate(li2):
    dict[i] = idx
    
for j in li:
    print(dict[j], end=' ')