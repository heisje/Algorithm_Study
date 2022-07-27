n = int(input())

cnt = n                         # 그룹 단어의 갯수

for i in range(n):              # n만큼 반복
    word = input()
    check = []                  # 그룹 단어를 판별하기 위한 check.list

    for j in word:              # word의 각 idx 반복
        if j not in check:      # j가 check.list에 없다면
            check.append(j)     # j를 check.list에 추가
        else:                   # j가 check.list에 있다면
            if j != check[-1]:  # j가 check.list에 마지막 idx와 같지 않다면 연속되지 않으므로 그룹단어 X
                cnt -= 1
                break           # 그룹단어가 아니라고 판별. 반복문멈춤

print(cnt)
