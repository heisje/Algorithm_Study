Big_paper = [[0 for j in range(100)] for i in range(100)] # 0이 가로, 세로 100개씩 들어있는 판을 만든다.

point_list = [[0, 0, 0, 0] for i in range(4)]
for i in range(4):
    point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3] = map(int, input().split()) # 입력 받은 데이터를 저장해둔다.

for i in range(4):
    for j in range(point_list[i][0] -1, point_list[i][0] -1 + (point_list[i][2] - point_list[i][0])): # 가로 길이
        for k in range(point_list[i][1] - 1, point_list[i][1] -1 + (point_list[i][3] - point_list[i][1])): # 세로 길이
            Big_paper[j][k] = 1 # 색종이를 덮은 곳을 1로 만든다.


count = 0
for i in range(100):
    for j in range(100):
        if Big_paper[i][j] == 1:
            count += 1

print(count)