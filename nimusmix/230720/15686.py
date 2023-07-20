from itertools import combinations

N, M = map(int, input().split())
min_value = 1e9
houses, chickens = [], []
distances = {}

for i in range(N):
    arr = list(map(int, input().split()))

    for j in range(N):
        if arr[j] == 1:
            houses.append((i, j))
        elif arr[j] == 2:
            chickens.append((i, j))
    
            
for hi, hj in houses:
    distances[(hi, hj)] = {}
    
    for ci, cj in chickens:
        distance = abs(hi - ci) + abs(hj - cj)
        distances[(hi, hj)][(ci, cj)] = distance
    
        
for combi in combinations(chickens, M):
    distance = 0
    
    for hi, hj in houses:
        min_distance = 1e9
        for ci, cj in combi:
            min_distance = min(min_distance, distances[(hi, hj)][(ci, cj)])
        distance += min_distance
        
        if min_value < distance:
            continue
        
    min_value = min(min_value, distance)

print(min_value)