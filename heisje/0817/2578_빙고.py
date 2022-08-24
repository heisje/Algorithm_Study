#https://www.acmicpc.net/problem/2578

# 빙고판 입력
li = []
check_li = [[0 for _ in range(5)] for _ in range(5)]
for _ in range(5):
    li.append(list(map(int, input().split())))

# 정답 리스트 받기
answer_li = []
for _ in range(5):
    answer_li.extend(list(map(int, input().split())))

# 빙고 확인하기
for idx, answer in enumerate(answer_li):
    binggo = 0 #빙고개수

    #전체반복하며 답에 있는 것을 체크리스트에 0 > 1로 바꾸어줌
    for y in range(5):
        for x in range(5):
            if li[y][x] == answer: 
                check_li[y][x] = 1 # 있으면 1로 만들어준다.

    #x축 빙고 확인            
    for y in range(5):
        if sum(check_li[y]) == 5:
            binggo += 1
    
    #y축 빙고 확인
    for x in range(5):
        sum_y = 0
        for y in range(5):
            sum_y += check_li[y][x]
        if sum_y == 5:
            binggo += 1
    
    #대각선 체크 diagonal이 대각선이래요
    diagonal = 0
    diagonal_reverse = 0
    for xy in range(5):
        diagonal += check_li[xy][xy]
        diagonal_reverse += check_li[4 - xy][xy] #반대 대각선
    if diagonal == 5:
        binggo += 1
    if diagonal_reverse == 5:
        binggo += 1

    #빙고가 3보다 크면
    if binggo >= 3:
        print(idx + 1)
        break
    
