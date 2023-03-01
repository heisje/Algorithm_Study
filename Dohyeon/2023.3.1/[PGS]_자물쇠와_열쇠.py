import copy

def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)

    # key2 = [[0 for _ in range(n)] for __ in range(n)]
    # key3 = [[0 for _ in range(n)] for __ in range(n)]
    # key4 = [[0 for _ in range(n)] for __ in range(n)]

    # 4가지 방향으로 확인하자

    key1 = []
    key2 = []
    key3 = []
    key4 = []

    holes = []

    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                holes.append((i, j))
    #
     #             key2[j][n - i - 1] = 1
    #             key3[n - i - 1][n - j - 1] = 1
    #             key4[n - j - 1][1] = 1

    for i in range(n):
        for j in range(n):
            if key[i][j] == 1:
                key1.append([i - n,j - n])
                key2.append([j - n, n - i - 1 - n])
                key3.append([n - i - 1 - n , n - j - 1 - n])
                key4.append([n - j - 1 - n , i - n])
            # n만큼 더 뺴줘서 키의 오른쪽 아래부터 차례로 확인하고자 하기 위함

    holes = set(tuple(holes))
    # key1 = set(key1)
    # key2 = set(key2)
    # key3 = set(key3)
    # key4 = set(key4)

    for i in range(n + m):
        for j in range(n + m):
            temp1 = copy.deepcopy(key1)
            temp2 = copy.deepcopy(key2)
            temp3 = copy.deepcopy(key3)
            temp4 = copy.deepcopy(key4)


            for k in range(len(key1)):


                temp1[k][0] = temp1[k][0] + i
                temp2[k][0] = temp2[k][0] + i
                temp3[k][0] = temp3[k][0] + i
                temp4[k][0] = temp4[k][0] + i

                temp1[k][1] = temp1[k][1] + j
                temp2[k][1] = temp2[k][1] + j
                temp3[k][1] = temp3[k][1] + j
                temp4[k][1] = temp4[k][1] + j

                temp1[k] = tuple(temp1[k])
                temp2[k] = tuple(temp2[k])
                temp3[k] = tuple(temp3[k])
                temp4[k] = tuple(temp4[k])

            temp1 = tuple(temp1)
            temp2 = tuple(temp2)
            temp3 = tuple(temp3)
            temp4 = tuple(temp4)

            if set(temp1) >= holes:
                temp1_list = list(set(temp1) - holes)
                for l in range(len(temp1_list)):
                    if 0 <= temp1_list[l][0] < m:
                        if 0 <= temp1_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp2) >= holes:
                temp2_list = list(set(temp2) - holes)
                for l in range(len(temp2_list)):
                    if 0 <= temp2_list[l][0] < m:
                        if 0 <= temp2_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp3) >= holes:
                temp3_list = list(set(temp3) - holes)
                for l in range(len(temp3_list)):
                    if 0 <= temp3_list[l][0] < m:
                        if 0 <= temp3_list[l][1] < m:
                            break
                else:
                    return True

            if set(temp4) >= holes:
                temp4_list = list(set(temp4) - holes)
                for l in range(len(temp4_list)):
                    if 0 <= temp4_list[l][0] < m:
                        if 0 <= temp4_list[l][1] < m:
                            break
                else:
                    return True


    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

"""
테스트 1 〉	통과 (1.53ms, 10.5MB)
테스트 2 〉	통과 (0.20ms, 10.4MB)
테스트 3 〉	통과 (153.00ms, 10.4MB)
테스트 4 〉	통과 (0.24ms, 10.4MB)
테스트 5 〉	통과 (35.02ms, 10.4MB)
테스트 6 〉	통과 (13.82ms, 10.3MB)
테스트 7 〉	통과 (316.55ms, 10.4MB)
테스트 8 〉	통과 (730.57ms, 10.6MB)
테스트 9 〉	통과 (221.30ms, 10.5MB)
테스트 10 〉	통과 (466.78ms, 10.6MB)
테스트 11 〉	통과 (1148.76ms, 10.5MB)
테스트 12 〉	통과 (0.07ms, 10.3MB)
테스트 13 〉	통과 (96.41ms, 10.4MB)
테스트 14 〉	통과 (9.87ms, 10.4MB)
테스트 15 〉	통과 (61.63ms, 10.4MB)
테스트 16 〉	통과 (133.81ms, 10.3MB)
테스트 17 〉	통과 (35.89ms, 10.4MB)
테스트 18 〉	통과 (136.14ms, 10.3MB)
테스트 19 〉	통과 (1.63ms, 10.4MB)
테스트 20 〉	통과 (361.28ms, 10.5MB)
테스트 21 〉	통과 (195.82ms, 10.6MB)
테스트 22 〉	통과 (81.74ms, 10.4MB)
테스트 23 〉	통과 (13.72ms, 10.4MB)
테스트 24 〉	통과 (7.63ms, 10.3MB)
테스트 25 〉	통과 (348.80ms, 10.4MB)
테스트 26 〉	통과 (1023.13ms, 10.6MB)
테스트 27 〉	통과 (1516.76ms, 10.5MB)
테스트 28 〉	통과 (105.28ms, 10.3MB)
테스트 29 〉	통과 (15.75ms, 10.3MB)
테스트 30 〉	통과 (144.32ms, 10.3MB)
테스트 31 〉	통과 (200.22ms, 10.4MB)
테스트 32 〉	통과 (795.66ms, 10.5MB)
테스트 33 〉	통과 (173.46ms, 10.4MB)
테스트 34 〉	통과 (7.58ms, 10.3MB)
테스트 35 〉	통과 (13.66ms, 10.3MB)
테스트 36 〉	통과 (10.45ms, 10.4MB)
테스트 37 〉	통과 (10.37ms, 10.4MB)
테스트 38 〉	통과 (1.45ms, 10.5MB)
"""