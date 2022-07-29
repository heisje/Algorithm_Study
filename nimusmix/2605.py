n = int(input())
m = list(map(int, input().split()))
line = []

# 번호표를 뽑은 학생이 들어가는 자리는 본인 위치에서 본인이 뽑은 번호를 뺀 자리와 같음.
for i in range(n):
    line.insert(i-m[i], i+1)

print(*line)