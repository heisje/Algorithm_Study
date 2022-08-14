#https://www.acmicpc.net/problem/1244

#문제:   1.스위치를 주고
#        2.성별이 남자일 때 -> 배수 스위치
#        3.성별이 여자일 때 -> 좌우 비교 스위치

#풀이방법: 남자일땐 %를 사용해서 배수체크, 여자일땐 스위치 기준으로 for를 돌려 검출
N = int(input())
switch = list(map(int, input().split()))
HU_NUM = int(input())

change = lambda a:abs(a-1)
for _ in range(HU_NUM):
    #입력 ( 성별, 스위치 위치 )
    gender, idx = map(int, input().split()) 

    #남자일 때
    if gender == 1:
        for i in range(len(switch)):
            if i % idx == idx - 1:
                switch[i] = change(switch[i])

    #여성일 때
    if gender == 2:
        idx -= 1
        if len(switch) - idx > idx: # 스위치 값이 중앙보다 작으면
            switch[idx] = change(switch[idx])
            for i in range(1, idx + 1): # 0~idx까지만 비교 후 변경
                if switch[idx - i] == switch[idx + i]: 
                    switch[idx - i] = change(switch[idx - i])
                    switch[idx + i] = change(switch[idx + i])
                else:
                    break
        else:                       # 스위치 값이 중앙보다 크면
            switch[idx] = change(switch[idx])
            for i in range(1, N - idx): #idx~HU_NUM까지만 비교 후 변경
                if switch[idx - i] == switch[idx + i]:
                    switch[idx - i] = change(switch[idx - i])
                    switch[idx + i] = change(switch[idx + i])
                else:
                    break
for i in range(0,len(switch),10): #이런 조건은 왜 있는거야 틀렸네
    print(*switch[i:i+10])
    
