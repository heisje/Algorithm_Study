import sys
input = sys.stdin.readline

def dfs(idx, total):
    global _max, _min
    if idx == N-1:                                  # 연산 다 하면
        _max = max(_max, total)                     # 최대, 최솟값 갱신
        _min = min(_min, total)
        return
    for i in range(4):                              # 연산자 4개 반복
        if operator[i]:                             # 연산할 연산자 남아있으면
            operator[i] -= 1                        # 연산할거니까 하나 뺌
            if i == 0:
                tmp = total + numbers[idx+1]
            elif i == 1:
                tmp = total - numbers[idx+1]
            elif i == 2:
                tmp = total * numbers[idx+1]
            elif i == 3:
                tmp = int(total / numbers[idx+1])
            dfs(idx+1, tmp)                         # 재귀
            operator[i] += 1                        # 원상복귀

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
_max = -float('inf')
_min = float('inf')
dfs(0, numbers[0])
print(_max)
print(_min)