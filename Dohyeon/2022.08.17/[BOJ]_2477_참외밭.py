# 해결 아이디어 : 가장 긴 두 곳에 붙어있는 짧은 길이들을 파악한다.

density = int(input())
lines = 6

longest_x = 0
longest_y = 0
len_list = []

for l in range(lines):
    dir, length = map(int, input().split())
    len_list.append(length)
    if dir == 1 or dir == 2:
        if length > longest_x:
            longest_x = length

    elif dir == 3 or dir == 4:
        if length > longest_y:
            longest_y = length

idx_x = len_list.index(longest_x)
if idx_x == len(len_list) - 1:              # 마지막 인덱스에 위치할 경우 인덱스 에러 방지
    if len_list[0] == longest_y:            # 가장 긴 x길이에 붙어있는 변 중 가장 긴 y길이가 아닌 쪽이 원하는 값
        target_y = len_list[-2]
    else:
        target_y = len_list[0]
else:
    if len_list[idx_x + 1] == longest_y:    # 가장 긴 x길이에 붙어있는 변 중 가장 긴 y길이가 아닌 쪽이 원하는 값
        target_y = len_list[idx_x - 1]
    else:
        target_y = len_list[idx_x + 1]

idx_y = len_list.index(longest_y)           # 같은 방법으로 원하는 x 값을 찾아냄
if idx_y == len(len_list) - 1:              # 마지막 인덱스에 위치하는 경우 인덱스 에러 방지
    if len_list[0] == longest_x:
        target_x = len_list[-2]
    else:
        target_x = len_list[0]
else:
    if len_list[idx_y + 1] == longest_x:
        target_x = len_list[idx_y - 1]
    else:
        target_x = len_list[idx_y + 1]


area = longest_x * longest_y - (longest_x - target_x) * (longest_y - target_y) # 원하는 넓이를 구한 후 밀도를 곱해준다.
print(area * density)

