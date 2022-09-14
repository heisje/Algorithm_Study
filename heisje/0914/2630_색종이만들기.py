import sys

def print_result(result): #결과 출력
    for a in result:
        print(a)

# 9칸 비교후, 결과값을 저장하는 새로운 배열을 만들어서 가보자고

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

result = [0, 0] #결과값

# N = 1일 경우 처리
if N == 1:  
    result[0+arr[0][0]] += 1
    print_result(result)
    exit()

# N >= 2일 경우 처리
n = N
while True:
    if n == 1:  # n이 1이 될경우 break
        if arr[0][0] != -2:
            result[0+arr[0][0]] += 1
        print_result(result)
        exit()
    next_arr = [[-2] * (n//2) for _ in range(n//2)]
    for by in range(n//2):
        for bx in range(n//2):
            # sub arr에 집어넣기
            save = arr[by*2][bx*2]
            check = True
            result_sub = [0, 0]
            for y in range(2): 
                for x in range(2):
                    temp = arr[by*2+y][bx*2+x]
                    if temp != -2:
                        result_sub[0+arr[by*2+y][bx*2+x]] += 1
                    if arr[by*2+y][bx*2+x] != save:
                        check = False
            
            if check is True: # 다 똑같으면 종이를 다음으로 넘긴다.
                next_arr[by][bx] = save
            if check is False: # 다르면, 종이를 더해준다.
                for i in range(2):
                    result[i] += result_sub[i]
    arr = next_arr
    n = n//2
