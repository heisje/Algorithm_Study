# 핵심 : 가장 높은 건물 기준으로 계단식으로 올라갔다 내려온다. 건물 사이의 거리만큼을 곱해서 거리를 구한다.
import sys
# 방법 : 최대값을 가진곳 까지 가장 높은 높이로 넓이를 구한다.
         #반대쪽의 경우 인덱스를 맨 뒤부터 최대값을 가진 곳 까지 구한다.

N = int(input())

pillars = []      #기둥입력받기
for n in range(N):
    pillars.append(tuple(map(int,sys.stdin.readline().split())))
pillars.append((1001,0)) #마지막 값 생성해두기
pillars.sort()

max_index, max_height = max(pillars, key=lambda a:a[1]) # 최대값을 가진 곳을 찾는다.
sum_height = max_height # 모든 합계
col = 0 #곱해질 기둥높이 (y)
idx_save = 0 #높은 위치를 저장하기 위해

for idx in range(len(pillars) - 1): #왼쪽 기둥보다 높으면 다음 기둥까지 사각형
    if pillars[idx][0] < max_index: # 가장 높은 기둥보다 낮을 경우
        if pillars[idx][1] > col: # 지붕 높이 검출
            col = pillars[idx][1]
        sum_height += abs(pillars[idx][0] - pillars[idx + 1][0]) * col #두 기둥의 x 차이를 높이로
    else:
        idx_save = idx #가장 높은 인덱스 저장
        break
col = 0
for idx in range(len(pillars)-1, idx_save,-1): #왼쪽 기둥보다 높으면 다음 기둥까지 사각형
    if pillars[idx][1] > col: # 지붕 높이 검출
        col = pillars[idx][1]
    sum_height += abs(pillars[idx - 1][0] - pillars[idx][0]) * col
        
print(sum_height)