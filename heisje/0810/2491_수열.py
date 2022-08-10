N = int(input())
li = map(int,input().split())
check_up = 0          #올라가는 개수 체크
check_down = 0        #내려가는 개수 체크
last_value = 0        #마지막 수 저장
maxi = 0              #최대값

#리스트를 지나면서 올라가는지 내려가는지 체크
for num in li:  
    if num >= last_value: #올라가는지 체크
        check_up +=1
    else :
        check_up = 1
    if num <= last_value: #내려가는지 체크
        check_down +=1
    else :
        check_down = 1
    if maxi < check_up or maxi < check_down: #최대값 체크
        maxi = max(check_up, check_down)
    last_value = num
print(maxi)