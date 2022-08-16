import sys
input = sys.stdin.readline

K = int(input())
arr = [list(map(int, input().split()))for _ in range(6)]
# max_C, max R 은 큰 사각형의 가로, 세로
# c, r 은 작은 사각형의 가로, 세로
max_C = max_R = c = r = 0

for i in range(6):
    if arr[i][0] < 3:                                       # 동, 서 방향 세로 탐색
        if arr[i][1] > max_C:                               # 큰 사각형 세로 길이 구하기
            max_C = arr[i][1]
            # max 길이가 나오고 +-3번째에 작은 사각형의 가로변의 길이가 나옴.
            # i의 범위는 0~5 이므로 0~2는 +3, 3~5는 -3번째 인덱스를 탐색.
            c = arr[i-3][1] if i > 2 else arr[i+3][1]
    else:                                                   # 남, 북 방향 가로 탐색
        if arr[i][1] > max_R:                               # 큰 사각형 가로 길이 구하기
            max_R = arr[i][1]
            # max 길이가 나오고 +-3번째에 작은 사각형의 세로변의 길이가 나옴.
            # i의 범위는 0~5 이므로 0~2는 +3, 3~5는 -3번째 인덱스를 탐색.
            r = arr[i-3][1] if i > 2 else arr[i+3][1]

# 큰 사각형 넓이에서 작은 사각형 넓이 빼고 참외 갯수 곱하기
print((max_C * max_R - c * r) * K)