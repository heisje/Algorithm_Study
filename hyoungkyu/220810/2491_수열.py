# 152ms

N = int(input())
num = list(map(int, input().split()))
lst = []

if N == 1:  # 예외 처리
    lst = [1]
else:
    for i in range(N-1):  # num의 요소가 증가 or 감소 or 같은 경우에 따른 리스트 생성 (lst의 크기 = N-1)
        if num[i] - num[i+1] > 0:
            lst.append(1)
        elif num[i] - num[i+1] < 0:
            lst.append(-1)
        else:
            lst.append(0)
'''(ex)
N = 9
num = [1, 2, 2, 4, 4, 5, 7, 7, 2]
lst = [1, 0, 1, 0, 1, 1, 0, -1]

N = 9
num = [4, 1, 3, 3, 2, 2, 9, 2, 3]
lst = [-1, 1, 0, -1, 0, 1, -1, 1]
'''

posi = 0
negi = 0
if lst[0] == 1:  # lst의 처음 값에 따른 posi, negi 초기값 지정
    posi = 1
elif lst[0] == -1:
    negi = 1
else:
    posi = 1
    negi = 1
cnt = 0  # 총 개수를 출력할 변수 선언

for i in range(1, N-1):  # lst의 값에 따른 cnt 계산
    if lst[i] == 1:
        negi = 0
        posi += 1
        if posi >= cnt:
            cnt = posi
    elif lst[i] == -1:
        posi = 0
        negi += 1
        if negi >= cnt:
            cnt = negi
    else:
        posi += 1
        negi += 1
        if posi >= cnt:
            cnt = posi
        elif negi >= cnt:
            cnt = negi
print(cnt+1)  # 각 값들의 차이로 리스트를 생성했으므로 최종 연속하는 숫자의 개수를 구할때는 +1을 해줘야함