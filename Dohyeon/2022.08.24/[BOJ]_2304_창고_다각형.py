import sys

N = int(sys.stdin.readline())

tops = {}

for lines in range(N):
    L, H = map(int, sys.stdin.readline().split())
    tops[L] = H

pos = list(tops.keys())                     # 기둥의 위치 리스트

pos.sort()

area = 0
now = 0
max_height = 0
max_height_pos = 0


for i in range(len(pos)):                   # 가장 높은 길이와 그 위치를 찾자
    if tops[pos[i]] >= max_height:          # 가장 긴 것이 여러개라면 뒤의 값을 기준으로 잡자
        max_height = tops[pos[i]]
        max_height_pos = i


while(True):                                # 올라가는 중
    for i in pos[now + 1:]:
        if tops[i] > tops[pos[now]]:
            area += (i - pos[now])*tops[pos[now]]
            now = pos.index(i)
            break
    if now == max_height_pos:
        break

area += max_height                      # 가장 긴 기둥부터는 기둥 오른쪽을 기준으로 생각하자, 가장 긴 기둥은 그러면 가로 길이 1을 더 가진다

new_pos = pos[::-1]
now = 0
max_height = 0
while(True):                            # 내려가는 중
    for i in new_pos[now + 1:]:
        if tops[i] > tops[new_pos[now]]:
            area += (new_pos[now] - i) * tops[new_pos[now]]
            now = new_pos.index(i)
            break
    if now == max_height_pos:
        break

print(area)







