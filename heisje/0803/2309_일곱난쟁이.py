#https://www.acmicpc.net/problem/2309
#    30840KB    68ms

#9난장이의 키를 입력받는다.
#핵심 : 9난장이의 키의 총 합에서, 두 사람이 빠지면 키가 100이 되는 것을 사용하였다.
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