# 아이디어 : 제곱수 3개까지를 그냥 전부 더해서 체크해본다.....

# 종료조건 빡세게 달면 파이썬에서 될 것도 같았지만, 4개짜리 공식이 있는 것을 보고 포기

from math import sqrt
N = int(input())

if sqrt(N) % 1 == 0:
    print(1)
else:
    plus = 0
    for i in range(int(sqrt(N))+1): 
        for j in range(int(sqrt(N))+1): 
            for k in range(int(sqrt(N))+1): 
                # i=0, j=0, k=정수인 경우 plus가 0이여서 총 합이 1부터 다 찾고
                # i=0, j=정수, k=정수인 경우 plus가 1이여서 총 합이 2를 다 찾고 ...
                find = i**2 + j**2 + k**2
                if find == N: 
                    print(1+plus)     
                    exit() # 1개일때, 2개일때, 3개일때 순서대로 찾아지므로 exit
                if find > N: # 그나마 시간 줄이기
                    break
            if plus == 0: # j가 0에서 1이 될 때 2개짜리 찾는 것
                plus = 1
        plus = 2 # i가 0에서 1이 될 때 3개짜리 찾는 것
    print(4)

#pypy제출 / 실버3 / 144ms / 2시간