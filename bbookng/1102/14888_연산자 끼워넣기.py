import sys
input = sys.stdin.readline

def dfs(idx, total):
    global _max, _min
    if idx == N-1:
        _max = max(_max, total)
        _min = min(_min, total)
        return
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                tmp = total + numbers[idx+1]
            elif i == 1:
                tmp = total - numbers[idx+1]
            elif i == 2:
                tmp = total * numbers[idx+1]
            elif i == 3:
                tmp = int(total / numbers[idx+1])
            dfs(idx+1, tmp)
            operator[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
_max = -float('inf')
_min = float('inf')
dfs(0, numbers[0])
print(_max)
print(_min)