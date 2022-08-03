arr = [int(input()) for _ in range(9)]

for i in arr:
    for j in arr:
        if i != j:                          # 같은 수를 2번 더할 수 있으므로 해당 경우의 수 제외
            if sum(arr) - (i+j) == 100:     # 총 합에서 두 난쟁이의 키를 뺐을 때 100이 되는 경우
                arr.remove(i)               # 두 난쟁이를 arr에서 제거
                arr.remove(j)
                break


arr = sorted(arr)                           # 키 순으로 정렬
print(*arr, sep = '\n')