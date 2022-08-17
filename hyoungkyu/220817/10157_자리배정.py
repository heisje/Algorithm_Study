# 1092ms

C, R = map(int, input().split())
lst = [[0]*C for _ in range(R)]  # RxC 행렬 생성
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌

lst[R-1][0] = 1  # 1,1에 값 추가

row = R-1  # 첫 위치 지정
col = 0

cnt = 2  # 넣을 값 지정
rot = 0  # 처음 이동할 방향 지정
key = int(input())  # 찾을 값 입력

if key == 1:  # 찾을 값이 1일때 출력
    print('1 1')
elif key <= C*R:  # 찾을 값이 유효하면
    while cnt <= C*R:
        if 0 <= row + d[rot][0] < R and 0 <= col + d[rot][1] < C:  # 행렬 범위 내에서
            if lst[row + d[rot][0]][col + d[rot][1]] == 0:  # 이미 입력된 값이 아니면
                lst[row + d[rot][0]][col + d[rot][1]] = cnt  # 새로운 값 입력
                row += d[rot][0]  # 다음 위치 지정
                col += d[rot][1]
                if cnt == key:  # 목표값을 찾으면 좌표를 출력하고 멈춤
                    print(col + 1, R - row)
                    break
                cnt += 1  # 목표값이 아니면 다음 값을 위해 +1
            else:
                rot = (rot + 1) % 4  # 이미 입력된 값이 있으면 방향 틀기
        else:
            rot = (rot + 1) % 4  # 행렬 밖으로 벗어나려고 하면 방향 틀기
else:
    print(0)  # 찾을 값이 유효하지 않으면 0 출력
