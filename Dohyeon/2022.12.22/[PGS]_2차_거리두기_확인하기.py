def solution(places):
    answer = []
    for tc in range(len(places)):
        check = False
        for i in range(5):
            if check:
                break
            for j in range(5):
                if check:
                    break
                if places[tc][i][j] == 'P':
                    a = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    b = [(-2, 0), (0, 2), (2, 0), (0, -2)]
                    c = [(-1, -1,), (-1, 1), (1, 1), (1, -1)]

                    for dr in a:
                        new_i = i + dr[0]
                        new_j = j + dr[1]
                        if new_i < 0 or new_j <0 or new_i > 4 or new_j > 4 :
                            continue
                        if places[tc][new_i][new_j] == 'P':
                            check = True
                            answer.append(0)
                            break
                    if check:
                        break

                    for k in range(len(b)):
                        new_i = i + b[k][0]
                        new_j = j + b[k][1]
                        if new_i < 0 or new_j < 0 or new_i > 4 or new_j > 4:
                            continue
                        if places[tc][new_i][new_j] == 'P':
                            if places[tc][i + a[k][0]][j + a[k][1]] == 'O':
                                check = True
                                answer.append(0)
                                break
                    if check:
                        break
                    for k in range(len(c)):
                        new_i = i + c[k][0]
                        new_j = j + c[k][1]
                        if new_i < 0 or new_j < 0 or new_i > 4 or new_j > 4:
                            continue
                        if places[tc][new_i][new_j] == 'P':
                            """
                            if places[tc][i + a[k][0]][j + a[k][1]] == 'O' or places[tc][i + a[k - 1][0]][j + a[k - 1][1]] == 'O':
                                check = True
                                answer.append(0)
                                break
                            """
                            if k == 0:
                                if places[tc][new_i + 1][new_j] == 'O' or places[tc][new_i][new_j + 1] == 'O':
                                    check = True
                                    answer.append(0)
                                    break
                            elif k == 1:
                                if places[tc][new_i + 1][new_j] == 'O' or places[tc][new_i][new_j - 1] == 'O':
                                    check = True
                                    answer.append(0)
                                    break

                            elif k == 2:
                                if places[tc][new_i - 1][new_j] == 'O' or places[tc][new_i][new_j - 1] == 'O':
                                    check = True
                                    answer.append(0)
                                    break

                            elif k == 3:
                                if places[tc][new_i - 1][new_j] == 'O' or places[tc][new_i][new_j + 1] == 'O':
                                    check = True
                                    answer.append(0)
                                    break
            if check:
                break
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOP", "POXPO"], ["PXPOO","XPXOO","PXOOO","OOOOO","OOPOP"]]))
