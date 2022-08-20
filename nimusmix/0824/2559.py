N, K = map(int, input().split())
temp = list(map(int, input().split()))
maxT = -999999999999999
sumT = 0

for i in range(N-K+1):
    if i == 0:
        sumT = sum(temp[i:i+K])
    else:
        sumT = sumT - temp[i-1] + temp[i+K-1]
        
    if sumT > maxT:
        maxT = sumT
        
print(maxT)