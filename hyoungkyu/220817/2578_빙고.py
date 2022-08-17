# 72ms

import sys
input = lambda: sys.stdin.readline().strip()

bingo = [list(map(int, input().split())) for _ in range(5)]  # 빙고 리스트
cnt = 0  # 수의 순서
bing = 0  # bingo 수
lst = [[],[],[],[]] # 이미 체크한 줄 입력(가로, 세로, 대각1, 대각2)

flag = False
for _ in range(5):
    call = list(map(int, input().split()))
    for k in call:    
        for i in range(5):
            if k in bingo[i]:
                tmp = bingo[i].index(k)             # 열의 인덱스 저장
                bingo[i][tmp] = 0                   # 불러진 수를 0으로 바꿈
                cnt += 1                            # 수의 개수 증가
                
                for j in range(5):                  # 가로
                    if bingo[i][j] == 0:
                        pass
                    else:
                        break
                else:
                    if i not in lst[0]:             # 이미 체크한 빙고 제외
                        bing += 1
                        lst[0].append(i)
                    if bing >= 3:                   # 빙고가 3개 이상이면 끝
                        flag = True
                        break

                for j in range(5):                  # 세로
                    if bingo[j][tmp] == 0:
                        pass
                    else:
                        break
                else:
                    if tmp not in lst[1]:           # 이미 체크한 빙고 제외
                        bing += 1
                        lst[1].append(tmp)
                    if bing >= 3:                   # 빙고가 3개 이상이면 끝
                        flag = True
                        break

                for j in range(5):                  # 대각선 1
                    if bingo[j][j] == 0:
                        pass
                    else:
                        break
                else:
                    if 0 not in lst[2]:             # 이미 체크한 빙고 제외
                        bing += 1
                        lst[2].append(0)
                    if bing >= 3:                   # 빙고가 3개 이상이면 끝
                        flag = True
                        break

                for j in range(5):                  # 대각선 2
                    if bingo[j][4-j] == 0:
                        pass
                    else:
                        break
                else:
                    if 0 not in lst[3]:             # 이미 체크한 빙고 제외
                        bing += 1
                        lst[3].append(0)
                    if bing >= 3:                   # 빙고가 3개 이상이면 끝
                        flag = True
                        break

            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break
print(cnt)