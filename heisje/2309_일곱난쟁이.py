#https://www.acmicpc.net/problem/2309
#    30840KB    68ms

#9난장이의 키를 입력받는다.
#9난장이의 키의 총 합에서, 두 사람이 빠지면 키가 100이 되는 것을 사용하였다.
#두 사람의 인덱스 값을 저장하여, 프린트할 때 빼버렸다.

#입력
height = [None]*9                   #모든 키의 리스트
sum_height = 0                      #키의 총 합
for i in range(9):
    height[i] = int(input())
    sum_height += height[i]

#정렬
height.sort()         

#찾기
save_i = save_j = 0
for i in range(9):
    for j in range(1, 9):
        if i < j:
            if sum_height - height[i] - height[j] == 100:
                #print(height[i], height[j])
                save_i = i
                save_j = j

#출력                
for hei in height:
    if hei != height[save_i] and hei != height[save_j]:
        print(hei)

'''
def forfor(height, check_list, count, answer, n):
    if n == 0 :
        return 
    for i in range(n):
        if check_list[i] == False:
            if count == 100:
                for ans in answer:
                    print(ans)
                    return
            check_list[i] = True
            count += height[i]
            answer.append(height[i])
            forfor(height, check_list, count, answer, n - 1)
            answer.pop
            check_list[i] = False
            count -= height[i]
    return

height = [None]*9
for i in range(9):
    height[i] = int(input())

height.sort()
check_list = [False for _ in range(len(height))] 
count = 0
forfor(height, check_list, count, [], 9)
'''
