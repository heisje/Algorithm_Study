#https://www.acmicpc.net/problem/2563
#	30840	76ms

#방법 1. 2차원 리스트에 1과 0을 채워서 1의 값을 구한다.
#방법 2. 도화지의 x,y값을 기준으로 겹치는 구간을 구해서 빼준다.

#방법 2가 더 빠를 것 같은데, 방법1을 사용하였다.



def list_on(li, x, y):                #li에 x,y축을 기준으로 10x10을 1로 바꾸어 세는 함수
    count = 0
    for yy in range(y, y + 10):
        for xx in range(x, x + 10):
            if li[yy][xx] == 0:
                count += 1
            li[yy][xx] = 1
    return count


N = int(input())                                    #사각형 개수입력받기
li = [[0 for _ in range(101)] for _ in range(101)]  #100크기의 사각형을 생성해놓는다.

count = 0
for _ in range(N):                                  #사각형 개수만큼 반복
    x, y = map(int, input().split())                #x y입력받기
    count += list_on(li, x, y)                      
print(count)