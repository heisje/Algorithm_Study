N = int(input())

_max = 0

for i in range(1, N+1): # 1부터 N까지 2번째 수를 넣어봄
    arr = [N, i]
    while True:
        if arr[-2] - arr[-1] < 0: # 다음 수가 음수라면 break
            break
        arr.append(arr[-2]-arr[-1]) #다음 수가 음수가 아니라면 arr 뒤에 해당 수를 넣음

    if _max < len(arr): # 위 while문이 끝나고 arr의 길이를 확인했을 때, 최대값보다 길다면
        _max = len(arr) # 최대값을 갱신
        result = arr    # result를 갱신

print(_max)
print(*result)



