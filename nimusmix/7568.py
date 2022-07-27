n = int(input())
people = []
rank = []

for i in range(n):
    kg, cm = map(int, input().split())
    people.append([kg, cm])

for i in range(n):
    count = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    rank.append(count+1)
    
print(*rank)