import sys
input= lambda: sys.stdin.readline().strip()

n = int(input())

for k in range(n):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.pop(0)
    arr2.pop(0)

    x = 4

    for i in range(4):
        if arr1.count(x) > arr2.count(x):
            print('A')
            break
        elif arr1.count(x) < arr2.count(x):
            print('B')
            break
        else:
            x -= 1
        if x == 0:
            print('D')


