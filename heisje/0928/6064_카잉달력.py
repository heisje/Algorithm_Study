import sys
input = lambda : sys.stdin.readline()
for _ in range(int(input())):
    M, N, x, y= map(int, input().split())
    if M > N:
        M, N = N, M
        x, y = y, x
    time = 0
    result = 0
    maxi = (M * N) 
    while True:
        #print(x,y)
        if x == y:
            result = x
            break
        if x < y:
            x += M
        elif x > y:
            y += N
        
        if x > maxi and  y > maxi:
            result = -1
            break
    print(result)

#    3 13    23 33
#    9    21    33
# 실버1 / 40분 / pypy3 224ms
