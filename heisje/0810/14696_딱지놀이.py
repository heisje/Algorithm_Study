N = int(input())

#A와 B의 모든 input
a_li = []
b_li = []

#입력
for _ in range(N):
    a_li.append(list(map(int, input().split()))[1:])
    b_li.append(list(map(int, input().split()))[1:])

#검증
for case in range(0, N):                                       #for 모든 케이스 검증
    for shape in range(4, 0, -1):                              #for 모양에 따른 갯수검사
        if a_li[case].count(shape) > b_li[case].count(shape):  #리스트 내의 숫자 비교
            print('A')
            break
        elif a_li[case].count(shape) < b_li[case].count(shape):
            print('B')
            break
    else:                                                      #결과가 똑같으면 print'D'
        print('D')
