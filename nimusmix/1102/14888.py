import sys
input = lambda: sys.stdin.readline().strip()
        
def dfs(i, result):
    global add, sub, mul, div, max_result, min_result
    
    if i == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if add > 0:
        add -= 1
        dfs(i + 1, result + numbers[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, result - numbers[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, result * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, int(result / numbers[i]))
        div += 1

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -10000000000
min_result = 10000000000

dfs(1, numbers[0])

print(max_result)
print(min_result)