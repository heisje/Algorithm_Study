import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())
point_list = [[0, 0, 0, 0] for i in range(N)]
max_num = 0

for i in range(N):
    point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3] = map(int, input().split())  # 입력 받은 데이터를 저장해둔다.
    for j in (range(4)):
        if point_list[i][j - 2] + point_list[i][j] > max_num:
            max_num = point_list[i][j - 2] + point_list[i][j] + 1

Big_paper = [[0 for j in range(max_num)] for i in range(max_num)]  # 0이 가로, 세로 max_num개씩 들어있는 판을 만든다.

for i in range(N):
    for j in range(point_list[i][0], point_list[i][0] + point_list[i][2]):  # 가로 길이
        for k in range(point_list[i][1], point_list[i][1] + point_list[i][3]):  # 세로 길이
            Big_paper[k][j] = i + 1  # 색종이를 덮은 곳을 색종이 숫자와 같게 만든다

count_list = []
for q in range(N):
    count = 0
    for i in range(max_num):
        for j in range(max_num):
            if Big_paper[i][j] == (q + 1):  # 보이는 색종이 넓이를 카운트한다.
                count += 1
    count_list.append(count)

for i in count_list:
    print(i)