import sys
input = lambda: sys.stdin.readline().strip()

X, Y = map(int, input().split())
N = int(input())

# 가장 넓은 X 공간과 Y공간을 곱하면된다.
x_list = [0]
y_list = [0]
for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        y_list.append(b) # 가로로 자른다 -> y축을 자른다.
    elif a == 1:
        x_list.append(b) # 세로로 자른다 -> x축을 자른다.
    else:
        print("버그입력")

if x_list[-1] != X: # 설마하지만 10cm짜리 종이의 10번째 줄을 자라는 명령이 오면 스킵
    x_list.append(X) # 그런것이 아니라면 종이의 원래 길이를 append
if y_list[-1] != Y:
    y_list.append(Y)
x_list.sort() # 정렬을 한 번 해줘야한다.
y_list.sort()
max_x = 0
max_y = 0
for i in range(len(x_list) - 1): # i + 1을 계산해야하므로 1을 빼줌
    if x_list[i + 1] - x_list[i] > max_x:
        max_x = x_list[i + 1] - x_list[i]

for i in range(len(y_list) - 1): # i + 1을 계산해야하므로 1을 빼줌
    if y_list[i + 1] - y_list[i] > max_y:
        max_y = y_list[i + 1] - y_list[i]
   
result = max_x*max_y
print(result)

