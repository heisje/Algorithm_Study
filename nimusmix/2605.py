n = int(input())
m = list(map(int, input().split()))
line = []

for i in range(n):
    line.insert(i-m[i], i+1)

print(*line)