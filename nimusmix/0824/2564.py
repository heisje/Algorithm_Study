X, Y = map(int, input().split())
N = int(input())
didx_li = [0] * (N+1)                                              # 입력 그대로 저장할 리스트
idx_li = [0] * (N+1)                                               # 좌표로 변환하여 저장할 리스트
dtc = 0                                                            # distance

for n in range(N+1):
    a, b = map(int, input().split())
    didx_li[n] = (a, b)
    
    if a == 1: idx_li[n] = (0, b)
    elif a == 2: idx_li[n] = (Y, b)
    elif a == 3: idx_li[n] = (b, 0)
    elif a == 4: idx_li[n] = (b, X)

for i in didx_li[:N+1]:                                            # didx_li와 idx_li의 마지막 원소는 현재 경비원의 위치이므로 제외하고 순회
    minX = min(i[1]+didx_li[-1][1], X-i[1]+X-didx_li[-1][1])       # [---(1)---|----(2)----] 중에 짧은 길이 져쟝
    minY = min(i[1]+didx_li[-1][1], Y-i[1]+Y-didx_li[-1][1])
    
    if i[0] == didx_li[-1][0]:                                     # 경비원의 방향과 상점의 방향이 같아 같은 선상에 위치하면,
        dtc += abs(i[1] - didx_li[-1][1])                          # 입력된 거리의 차이 만큼을 distance에 저장
    elif i[0] in [1, 2]:                                           # 상점이 남 or 북에 있을 때,
        if didx_li[-1][0] in [1, 2]:                               # 경비원도 북 or 남에 있으면
            dtc += Y + minX                                        # Y와 minX를 더하여 distance에 저장
        else:                                                      # 경비원이 동 or 서에 있으면 상점 좌표와 경비원 좌표의 x, y의 차이를 저장
            dtc += abs(idx_li[didx_li.index(i)][0]-idx_li[-1][0]) + abs(idx_li[didx_li.index(i)][1]-idx_li[-1][1])
    else:                                                          # 상점이 동 or 서에 있을 때,
        if didx_li[-1][0] in [3, 4]:                               # 경비원도 서 or 동에 있으면
            dtc += X + minY                                        # X와 minY를 더하여 distance에 저장
        else:                                                      # 경비원이 남 or 북에 있으면 상점 좌표와 경비원 좌표의 x, y의 차이를 저장
            dtc += abs(idx_li[didx_li.index(i)][0]-idx_li[-1][0]) + abs(idx_li[didx_li.index(i)][1]-idx_li[-1][1])
        
print(dtc)