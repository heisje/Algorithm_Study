N = int(input())
kg_list = []
cm_list = []
for i in range(N):
    kg, cm = map(int, input().split())
    kg_list.append(kg)
    cm_list.append(cm)

rank_list = []
for i in range(N):
    count = 1
    for j in range(N):
        if kg_list[i] < kg_list[j] and cm_list[i] < cm_list[j]:
            count += 1
    rank_list.append(count)
for i in rank_list:
    print(i, end=' ')