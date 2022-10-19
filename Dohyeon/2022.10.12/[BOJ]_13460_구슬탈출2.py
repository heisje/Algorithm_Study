
I, J = map(int, input().split())
matrix = []
found_R = False
found_B = False
R_i, R_j = 0, 0
B_i, B_j = 0, 0
for i in range(I):
    tmp = list(input())
    if (not found_R) or (not found_B):
        for j in range(J):
            if tmp[j] == "R":
                R_i, R_j = i, j
                found_R = True
            if tmp[j] == "B":
                B_i, B_j = i, j
                found_B = True
    matrix.append(tmp)

#print(matrix)
#print(R_i, R_j)
#print(B_i, B_j)
# 좌푤르 나타내는 딕셔너리와, 움직임을 나타내는 딕셔너리를 따로 두자
visited = {}        # 횟수를 저장할 사전 키는 R_i * 10**3 + R_j * 10**2 + B_i * 10**1 + B_j의 형태  어차피 인덱스는 9가 최대이므로
visited[R_i * 10**3 + R_j * 10**2 + B_i * 10**1 + B_j] = 0
tracking = {'':R_i * 10**3 + R_j * 10**2 + B_i * 10**1 + B_j}
result = -1                 # 최종결과
q = ['r', 'l', 'u', 'd']    # 시작 큐는 오른쪽, 왼쪽, 위, 아래를 넣어두자.
while(q):
    success_R = False  # 빨간 공 빼내기 성공확인용
    Trap_B = False     # 파란 공이 빠졌는지 확인용

    node = q.pop(0)
    if len(node) > 10:
        break
    num = tracking[node[:-1]]
    bf_R_i, bf_R_j, bf_B_i, bf_B_j = num//1000, (num//100)%10, (num//10)%10, num%10


    # 사이에 벽이나 구멍이 있는 예외처리
    row_mid_wall = False
    col_mid_wall = False
    if bf_R_i == bf_B_i:
        for j in range(min(bf_B_j, bf_R_j) + 1, max(bf_B_j, bf_R_j)):
            if matrix[bf_B_i][j] == "#" or matrix[bf_B_i][j] == "O":
                row_mid_wall = True
                break
    if bf_R_j == bf_B_j:
        for i in range(min(bf_B_i, bf_R_i) + 1, max(bf_B_i, bf_R_i)):
            if matrix[i][bf_R_j] == "#" or matrix[i][bf_R_j] == "O":
                col_mid_wall = True
                break

    new_num = -1
    #print(bf_R_i, bf_R_j, bf_B_i, bf_B_j, node, node[-1])
    if node[-1] == 'r':
        if bf_R_i == bf_B_i and not row_mid_wall:        # 같은 가로줄에 있을 경우
            if bf_R_j > bf_B_j:     # 빨간 공이 더 오른쪽에 있을 경우, 빨간 공 먼저 확인
                for j in range(bf_R_j, J):
                    if matrix[bf_R_i][j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[bf_R_i][j] == "#":
                        new_num = bf_R_i*1000 + (j - 1) * 100
                        break
                for j in range(bf_B_j, J):
                    if matrix[bf_B_i][j] == "O":
                        break
                    if matrix[bf_B_i][j] == "#":
                        new_num = new_num + bf_R_i*10 + (j - 2)
                        break
            else:                   # 파란 공이 더 오른쪽에 있을 경우
                for j in range(bf_B_j, J):
                    if matrix[bf_B_i][j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[bf_B_i][j] == "#":
                        new_num = bf_R_i * 10 + (j - 1)
                        break
                for j in range(bf_R_j, J):
                    if matrix[bf_R_i][j] == "O":
                        break
                    if matrix[bf_R_i][j] == "#":
                        new_num = new_num + bf_R_i * 1000 + (j - 2) * 100
                        break
        else:                       # 서로 다른 줄에 있을 경우
            for j in range(bf_R_j, J):
                if matrix[bf_R_i][j] == "O":
                    success_R = True    # 성공함
                    break
                if matrix[bf_R_i][j] == "#":
                    new_num = bf_R_i * 1000 + (j - 1) * 100
                    break
            for j in range(bf_B_j, J):
                if matrix[bf_B_i][j] == "O":
                    Trap_B = True       # 실패함
                if matrix[bf_B_i][j] == "#":
                    new_num = new_num + bf_B_i * 10 + (j - 1)
                    break





    elif node[-1] == 'l':
        if bf_R_i == bf_B_i and not row_mid_wall:        # 같은 가로줄에 있을 경우
            if bf_R_j > bf_B_j:     # 빨간 공이 더 오른쪽에 있을 경우, !!파란공!! 먼저 확인
                for j in range(bf_B_j, -1, -1):
                    if matrix[bf_B_i][j] == "O":
                        break
                    if matrix[bf_B_i][j] == "#":
                        new_num = bf_R_i*10 + (j + 1)
                        break

                for j in range(bf_R_j, -1, -1):
                    if matrix[bf_R_i][j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[bf_R_i][j] == "#":
                        new_num = new_num + bf_R_i*1000 + (j + 2) * 100
                        break

            else:                   # 파란 공이 더 오른쪽에 있을 경우

                for j in range(bf_R_j, -1, -1):
                    if matrix[bf_R_i][j] == "O":
                        break
                    if matrix[bf_R_i][j] == "#":
                        new_num = bf_R_i * 1000 + (j + 1) * 100
                        break

                for j in range(bf_B_j, -1, -1):
                    if matrix[bf_B_i][j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[bf_B_i][j] == "#":
                        new_num = new_num + bf_R_i * 10 + (j + 2)
                        break

        else:                       # 서로 다른 줄에 있을 경우
            for j in range(bf_R_j, -1, -1):
                if matrix[bf_R_i][j] == "O":
                    success_R = True    # 성공함
                    break
                if matrix[bf_R_i][j] == "#":
                    new_num = bf_R_i * 1000 + (j + 1) * 100
                    break
            for j in range(bf_B_j, -1, -1):
                if matrix[bf_B_i][j] == "O":
                    Trap_B = True       # 실패함
                if matrix[bf_B_i][j] == "#":
                    new_num = new_num + bf_B_i * 10 + (j + 1)
                    break


    elif node[-1] == 'u':
        if bf_R_j == bf_B_j and not col_mid_wall:        # 같은 세로줄에 있을 경우
            if bf_R_i < bf_B_i:     # 빨간 공이 더 위에 있을 경우, 빨간 공 먼저 확인
                for i in range(bf_R_i, -1, -1):
                    if matrix[i][bf_R_j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[i][bf_R_j] == "#":
                        new_num = (i + 1)*1000 + bf_R_j * 100
                        break
                for i in range(bf_B_i, -1, -1):
                    if matrix[i][bf_B_j] == "O":
                        break
                    if matrix[i][bf_B_j] == "#":
                        new_num = new_num + (i + 2)*10 + bf_B_j
                        break
            else:                   # 파란 공이 더 위에 있을 경우
                for i in range(bf_B_i, -1, -1):
                    if matrix[i][bf_B_j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[i][bf_B_j] == "#":
                        new_num = (i + 1) * 10 + bf_B_j
                        break
                for i in range(bf_R_i, -1, -1):
                    if matrix[i][bf_R_j] == "O":
                        break
                    if matrix[i][bf_R_j] == "#":
                        new_num = new_num + (i + 2) * 1000 + bf_R_j* 100
                        break
        else:                       # 서로 다른 줄에 있을 경우
            for i in range(bf_R_i, -1, -1):
                if matrix[i][bf_R_j] == "O":
                    success_R = True    # 성공함
                    break
                if matrix[i][bf_R_j] == "#":
                    new_num = (i + 1) * 1000 + bf_R_j * 100
                    break
            for i in range(bf_B_i, -1, -1):
                if matrix[i][bf_B_j] == "O":
                    Trap_B = True       # 실패함
                if matrix[i][bf_B_j] == "#":
                    new_num = new_num + (i + 1) *10 +  bf_B_j
                    break

    elif node[-1] == 'd':
        if bf_R_j == bf_B_j and not col_mid_wall:        # 같은 세로줄에 있을 경우
            if bf_R_i < bf_B_i:     # 빨간 공이 더 위에 있을 경우, !!파란공!! 먼저 확인
                for i in range(bf_B_i, I):
                    if matrix[i][bf_B_j] == "O":
                        break
                    if matrix[i][bf_B_j] == "#":
                        new_num = (i - 1)*10 + bf_B_j
                        break
                for i in range(bf_R_i, I):
                    if matrix[i][bf_R_j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[i][bf_R_j] == "#":
                        new_num = new_num + (i - 2)*1000 + bf_R_j * 100
                        break

            else:                   # 파란 공이 더 위에 있을 경우
                for i in range(bf_R_i, I):
                    if matrix[i][bf_R_j] == "O":
                        break
                    if matrix[i][bf_R_j] == "#":
                        new_num = (i - 1) * 1000 + bf_R_j* 100
                        break
                for i in range(bf_B_i, I):
                    if matrix[i][bf_B_j] == "O":    # 어차피 둘다 빠지게 되어있다.
                        break
                    if matrix[i][bf_B_j] == "#":
                        new_num = new_num + (i - 2) * 10 + bf_B_j
                        break

        else:                       # 서로 다른 줄에 있을 경우
            for i in range(bf_R_i, I):
                if matrix[i][bf_R_j] == "O":
                    success_R = True    # 성공함
                    break
                if matrix[i][bf_R_j] == "#":
                    new_num = (i - 1) * 1000 + bf_R_j * 100
                    break
            for i in range(bf_B_i, I):
                if matrix[i][bf_B_j] == "O":
                    Trap_B = True       # 실패함
                if matrix[i][bf_B_j] == "#":
                    new_num = new_num + (i - 1) *10 + bf_B_j
                    break



    if new_num == -1:
        continue
    else:
        if Trap_B:
            continue
        if success_R:
            result = len(node)
            break
        try:
            check = visited[new_num]
        except:
            visited[new_num] = visited[num] + 1
            tracking[node] = new_num
            if node[-1] == 'r':
                q.append(node + "r")
                q.append(node + "u")
                q.append(node + "d")
            elif node[-1] == 'l':
                q.append(node + "l")
                q.append(node + "u")
                q.append(node + "d")
            elif node[-1] == 'u':
                q.append(node + "r")
                q.append(node + "u")
                q.append(node + "l")
            elif node[-1] == 'd':
                q.append(node + "r")
                q.append(node + "d")
                q.append(node + "l")
print(result)


