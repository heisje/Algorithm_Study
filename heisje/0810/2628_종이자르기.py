M, N = map(int,input().split())
CASE = int(input())

x_li = []
y_li = []

for _ in range(CASE):
    axis, num = map(int,input().split())
    if axis == 0:
        y_li.append(num)
    if axis == 1:
        x_li.append(num)

x_li.sort()
y_li.sort()


x_max = 0
y_max = 0
end_num = 0
for x in x_li:
    if x - end_num > x_max:
        x_max = x - end_num
    end_num = x

if M - end_num > x_max:
    x_max = M - end_num

end_num = 0
for y in y_li:
    if y - end_num > y_max:
        y_max = y - end_num
    end_num = y
if N - end_num > y_max:
    y_max = N - end_num 

print(x_max * y_max)   
