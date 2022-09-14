import sys
def print_result(result): #결과 출력
    for a in result:
        print(a)

# 아이디어: 9칸 비교후, N//3만큼 작은 칸을 만들어서 반복한다. 그림판으로 설명하면 쉬울듯,,

N = int(input())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

result = [0, 0, 0] #결과값

# N = 1일 경우 처리
if N == 1:  
    result[1+arr[0][0]] += 1 # 1 0 -1 개수세기
    print_result(result)
    exit()

# N >= 3일 경우 처리
n = N
while True:
    # 종료조건
    if n == 1:  # n이 1이 될경우 exit
        if arr[0][0] != -2:          
            result[1+arr[0][0]] += 1 # 1 0 -1 개수세기
        print_result(result)
        exit()

    # 반복
    next_arr = [[-2] * (n//3) for _ in range(n//3)] # 다음 루프에 넘겨줄 n//3 해준 배열

    # 9등분으로 나누어서 y, x축 반복 (27일 경우 0 3 6 9 12 15 18)을 구하기위해서
    for by in range(n//3):
        for bx in range(n//3):
            # sub arr에 집어넣기
            save = arr[by*3][bx*3] # save = 첫번째 칸과 같은지 안같은지 체크 (etc: 3배해 준 이유,27일 경우 0 3 6 9 12 15 18)
            check = True           # check = 전체가 같은가?
            result_sub = [0, 0, 0] # 임시 합계
            for y in range(3):     # 9칸 체크
                for x in range(3):
                    temp = arr[by*3+y][bx*3+x]                  # 해당 칸 임시저장
                    if temp != -2:                              # 숫자가 들어있으면
                        result_sub[1+arr[by*3+y][bx*3+x]] += 1      # 임시 합계에 저장
                    if arr[by*3+y][bx*3+x] != save:             # 다른게 있으면
                        check = False
            
            if check is True:            # 다 똑같으면
                next_arr[by][bx] = save        # 다음 지도에 숫자를 집어넣어준다.
            if check is False:           # 다르면, 종이를 더해준다.
                for i in range(3):             
                    result[i] += result_sub[i]
    arr = next_arr # 한 턴이 끝났으니 다음 지도로
    n = n//3       # 지도의 최대 크기도 작게

    #실버 2 / 3시간