import sys
input = lambda : sys.stdin.readline()
N = int(input())
arr = list(map(int, input().split()))
dic = dict()
for idx, value in enumerate(sorted(set(arr))):
    dic[value] = idx
for a in arr:
    print(dic[a], end=" ")

# 실버2 / 10분 / 2076ms
