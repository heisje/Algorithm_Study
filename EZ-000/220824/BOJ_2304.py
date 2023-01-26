import sys

N = int(sys.stdin.readline())
pillars = []
maxH = 0        # 제일 높은 기둥의 높이
maxHL = 0       # 제일 높은 기둥의 왼쪽 면
maxL = 0        # 마지막 기둥의 왼쪽 면

# 입력 받아서 기둥 정보 리스트 만들면서 max 값 찾아주기
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    pillars.append([L, H])
    if H > maxH:
        maxH = H
        maxHL = L
    if L > maxL:
        maxL = L

# 기둥 높이 저장 리스트 생성
pList = [0] * (maxL + 1)
# 왼쪽 면을 인덱스로 높이 저장
for left, height in pillars:
    pList[left] = height

area = 0
tempH = 0       # 지역 최댓값 변수
# 1번부터 제일 높은 기둥까지
for idx in range(maxHL + 1):
    if pList[idx] > tempH:      # 현재 지역 최댓값보다 확인하는 기둥의 값이 더 높으면 갱신
        tempH = pList[idx]
    area += tempH
tempH = 0

for idx in range(maxL, maxHL, -1):
    if pList[idx] > tempH:
        tempH = pList[idx]
    area += tempH

print(area)
