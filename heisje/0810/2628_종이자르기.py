#핵심! 정렬 후 가장 큰 x값과 가장 큰 Y값을 구해서 곱한다!
M, N = map(int,input().split())
CASE = int(input())

x_li = []
y_li = []

#input받기
for _ in range(CASE): 
    axis, num = map(int,input().split())
    if axis == 0:
        y_li.append(num)
    if axis == 1:
        x_li.append(num)

#정렬하기
x_li.sort()
y_li.sort()

#x축 자르기
x_max = 0    #자른 최대값을 구하기 위해
end_num = 0  #처음부터 자르기 위해
for x in x_li:
    if x - end_num > x_max:
        x_max = x - end_num
    end_num = x

#마지막 부분 자르기
if M - end_num > x_max: #마지막은 따로 잘라줌
    x_max = M - end_num

#y축 자르기
y_max = 0
end_num = 0
for y in y_li:
    if y - end_num > y_max:
        y_max = y - end_num
    end_num = y
if N - end_num > y_max:
    y_max = N - end_num 

print(x_max * y_max)   
