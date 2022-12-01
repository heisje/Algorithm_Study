def line_test(line):
    ladder = [0]*N  # 사다리를 얹을 곳을 나타낼 visited같은 배열

    for i in range(1, len(line)):
        if line[i-1] == line[i]:  # 높이가 같으면 넘어가고
            pass
        else:  # 다른경우
            if line[i-1] - line[i] == 1:  # 내려가요
                for ladder_width in range(L):  # 내려가는 부분에 경사로 전부 넣기
                    if 0 <= i+ladder_width < N:  # 안에 있으면 정상적으로 경사로 on
                        if ladder[i+ladder_width] == 0:
                            ladder[i+ladder_width] = 1
                        else:
                            return 0    # 이미 1이면 비정상
                    else:           
                        return 0    # 밖이면 비정상 0
            elif line[i-1] - line[i] == -1:  # 올라가요
                for ladder_width in range(L):
                    if 0 <= i-1-ladder_width < N:
                        if ladder[i-1-ladder_width] == 0:
                            ladder[i-1-ladder_width] = 1
                        else:
                            return 0    # 이미 1이면 비정상
                    else: 
                        return 0    # 밖이면 비정상 0
            else: 
                return 0   # 두개이상 차이났을 때
    return 1  # 정상적인 경사로
        

N, L = map(int, input().split())
arr = list(list(map(int, input().split()))for _ in range(N))
arr_rev = list(map(list, zip(*arr)))
answer = 0
for n in range(N):
    answer += line_test(arr[n])
for n in range(N):
    answer += line_test(arr_rev[n])
print(answer)

# 골드3 / 80분 / 80ms