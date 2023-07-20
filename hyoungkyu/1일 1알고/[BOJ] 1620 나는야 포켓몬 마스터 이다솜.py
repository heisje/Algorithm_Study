import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_name = {}
dic_number = {}

for i in range(1, N+1):
    name = input()
    dic_name[name] = i
    dic_number[i] = name
for i in range(M):
    tmp = input()
    try:
        print(dic_number[int(tmp)], end='')
    except:
        print(dic_name[tmp])