import sys
input= lambda: sys.stdin.readline().strip()

n = int(input())

for k in range(n):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.pop(0)                                 # 첫 번째 수는 카드의 갯수라 뺌
    arr2.pop(0)

    x = 4                                       # 별부터 시작하니까 4부터 시작

    for i in range(4):
        if arr1.count(x) > arr2.count(x):
            print('A')
            break
        elif arr1.count(x) < arr2.count(x):
            print('B')
            break
        else:                                   # 똑같으면 다음 딱지로
            x -= 1
        if x == 0:                              # 끝까지 무승부면
            print('D')                          # 'D'


