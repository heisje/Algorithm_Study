#푸는 방법 = N 위아래로 체크하며, 만들 수 있는 최소값을 만날 때까지 해본다.
N = int(input()) #이동하려고 하는 채널
BREAK = int(input()) #고장난 버튼의 개수
all = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = set(map(int, input().split()))
b = sorted(list(all - b))
print(b)

len_N = len(str(N))
list_N = list(map(int, str(N)))
up = [b[0]] * len_N #가까운 가장 작은 숫자를 만들기 위해서 전부 가장 작은 숫자로 세팅, 올림도 예상해서
down = [b[-1]] * len_N

i = 0
#가장 앞에 수를 크게잡냐 작게잡냐로 나누자
if list_N[i] in b:
    down[i] = list_N[i]
    up[i] = list_N[i]
else:
    j = 0
    while True:
        if (list_N[i] + j) % 10 == 0:
            if b[0] == 0:
                down[i] = b[1]*10+b[0]
            else:
                down[i] = b[0]*10+b[0]
            break
        if (list_N[i] + j) % 10 in b: #큰값 찾기
            up[i] = (list_N[i] + j) % 10
            break
        j += 1
    j = 0
    while True:
        if (list_N[i] - j) % 10 == 0:
            down[i] = 0
            break
        if (list_N[i] - j) % 10 in b: #작은 값 찾기
            down[i] = (list_N[i] - j) % 10
            break
        j += 1

i = 1
while i < len_N:
    #가장 앞에 수를 크게잡냐 작게잡냐로 나누자
    if list_N[i] in b:
        down[i] = list_N[i]
        up[i] = list_N[i]
    else:
        j = 0
        while True:
            if (list_N[i] + j) % 10 in b:# 큰값 찾기
                up[i] = (list_N[i] + j) % 10
                break
            j += 1
        j = 0
        while True:
            if (list_N[i] - j) % 10 == 0:
                down[i-1] = down[-1] - 1
                down[i] =
            if (list_N[i] - j) % 10 in b: #작은 값 찾기
                down[i] = (list_N[i] - j) % 10
                break
            j += 1
    i += 1

print(int(''.join(map(str, up))))
print(N)
print(int(''.join(map(str, down))))
up = (int(''.join(map(str, up))) - N) + (len_N)
down = (N - int(''.join(map(str, down)))) + (len_N)
bbbbbb = abs(N - 100)

print(min(up, down, bbbbbb))


'''
N = int(input()) #이동하려고 하는 채널
BREAK = int(input()) #고장난 버튼의 개수
all = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
b = all - set(input().split())
#print(all, b)

num = 0
find = False


fast_search = []
for n in list(N):

while find is False:
    up = len(set(str(N + num)) - b)
    down = len(set(str(N - num)) - b)
    if up == 0:
        #print('+ find', str(N + num))
        fast_search.append(len(str(N + num)) + num)
        find = True
    if down == 0:
        #print('- find', str(N - num))
        fast_search.append(len(str(N - num)) + num)
        find = True
    num += 1

print(min(fast_search + [abs(N - 100)]))
'''