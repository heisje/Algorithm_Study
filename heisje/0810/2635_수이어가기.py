## 첫번째 숫자 입력받기
FIRST = int(input())

#0과 1일땐 그냥 값 내기
if FIRST == 0:
    print(3)
    print('0 1')
elif FIRST == 1:
    print(4)
    print('1 1 0 1')
else:
    #2 이상일때
    li = {}
    max_len = [3, 1]     #[최대길이, key값]

    #검증
    for i in range(FIRST // 2, FIRST):               #반 이상일때만 체크
        li[i] = [FIRST]                              #첫 숫자 고정상수
        li[i] += [i]                                 #두번째 숫자 i
        l_len = 2                                    #길이체크변수

        while True:                                  #행렬 검사
            if li[i][-2] - li[i][-1] >= 0:           #양일 경우
                li[i].append(li[i][-2] - li[i][-1])  #행렬에 추가, 길이도 + 1
                l_len += 1
            else:
                break
        if l_len > max_len[0]:                       #최대길이이면 저장
            max_len[0] = l_len
            max_len[1] = i

    print(max_len[0])
    print(*li[max_len[1]])
