w, h = map(int, input().split())
N = int(input())

w_list = [0, h]
h_list = [0, w]

for _ in range(N):
    a, b = map(int, input().split())
    
    w_list.append(b) if a == 0 else h_list.append(b)       # 가로 세로 구분하여 각 리스트에 추가

w_list.sort()
h_list.sort()

max_w = 0
max_h = 0

for c in w_list, h_list:
    for idx, i in enumerate(c):
        try:                                               # IndexError 발생하더라도 진행하기 위해 try-except 사용
            diff = abs(i-c[idx+1])                         # 리스트 값들의 차이를 변수 diff에 저장

            if c == w_list:
                if diff > max_h:                           # diff가 max보다 크면 max에 diff 값을 할당
                    max_h = diff
            else:
                if diff > max_w:
                    max_w = diff
        except:
            pass
            
print(max_w * max_h)