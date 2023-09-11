def solution(alp, cop, problems):
    max_req, max_cop = alp, cop
    for problem in problems:
        max_req = max(max_req, problem[0])
        max_cop = max(max_cop, problem[1])
    print(max_req, max_cop)
    DP = [[float('INF')] * (max_cop+1) for _ in range(max_req+1)]
    DP[alp][cop] = 0
    for i in range(alp, max_req+1):
        for j in range(cop, max_cop+1):
            if i < max_req:
                DP[i+1][j] = min(DP[i+1][j], DP[i][j] + 1)
            if j < max_cop:
                DP[i][j+1] = min(DP[i][j+1], DP[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_req)
                    new_cop = min(j+cop_rwd, max_cop)
                    DP[new_alp][new_cop] = min(DP[new_alp][new_cop], DP[i][j] + cost)

    print(DP[max_req][max_cop])
    return DP[max_req][max_cop]

            # for idx in range(len(problems)):
            #     if check[idx]: continue
            #     if i >= problems[idx][0] and j >= problems[idx][1]:
            #         possibles.append(problems[idx][2:5])
            #         check[idx] = True
            #         cnt -= 1
            #         if cnt == 0:
            #             for ik in range(alp, max_req+1):
            #                 for jk in range(cop, max_cop+1):
            #                     print(DP[ik][jk], end=' ')
            #                 print()
            #             print(DP[max_req][max_cop])
            #             return DP[max_req][max_cop]

            # for possible in possibles:
            #     if i+possible[0] > max_req or j+possible[1] > max_cop: continue
            #     DP[i+possible[0]][j+possible[1]] = min(DP[i][j] + possible[2], DP[i+possible[0]][j+possible[1]])


# def get_power(alp, cop, problems, check, possibles, answer):
#     min_v = 150
#     min_idx = -1
#     for i in range(len(problems)):
#         # 이미 추가한거는 건너뛰기
#         if check[i]:
#             continue
#         # 풀 수 있으면 ㄱㄱ
#         if problems[i][0] <= alp and problems[i][1] <= cop:
#             check[i] = True
#             possibles.append(problems[i][2:5])
#             if len(possibles)-2 == len(problems):
#                 return (alp, cop, answer)
#             return (alp+problems[i][2], cop+problems[i][3], answer+problems[i][4])
#         # 남은 문제들 중 가장 금방 풀 수 있는거 찾기
#         for j in range(len(possibles)):
#             tmp_v = 0
#             tmp_alp = problems[i][0] - alp
#             tmp_cop = problems[i][1] - cop
#             if tmp_alp <= 0 and tmp_cop > 0:
#                 while True:
#                     tmp_v += possibles[j][2]
#                     tmp_alp -= possibles[j][0]
#                     tmp_cop -= possibles[j][1]
#                     if tmp_alp <= 0 and tmp_cop <= 0:
#                         if min_v > tmp_v:
#                             min_v = tmp_v
#                         elif min_v == tmp_v and (min_idx == -1 or possibles[min_idx][0] <= possibles[j][0]):
#                             min_idx = j
#                         break
#                     if (tmp_alp <= 0 and possibles[j][1] == 0) or (tmp_cop <= 0 and possibles[j][0] == 0):
#                         break
#                 print(1, min_v, possibles[j], problems[i])

#             elif tmp_cop <= 0 and tmp_alp > 0:
#                 while True:
#                     tmp_v += possibles[j][2]
#                     tmp_alp -= possibles[j][0]
#                     tmp_cop -= possibles[j][1]
#                     if tmp_alp <= 0 and tmp_cop <= 0:
#                         if min_v > tmp_v:
#                             min_v = tmp_v
#                         elif min_v == tmp_v and (min_idx == -1 or possibles[min_idx][1] <= possibles[j][1]):
#                             min_idx = j
#                         break
#                     if (tmp_alp <= 0 and possibles[j][1] == 0) or (tmp_cop <= 0 and possibles[j][0] == 0):
#                         break
#                 print(2, min_v, possibles[j], problems[i])

#             else:
#                 while True:
#                     tmp_v += possibles[j][2]
#                     tmp_alp -= possibles[j][0]
#                     tmp_cop -= possibles[j][1]
#                     if tmp_alp <= 0:
#                         if min_v > tmp_v:
#                             min_v = tmp_v
#                         elif min_v == tmp_v and (min_idx == -1 or possibles[min_idx][1] <= possibles[j][1]):
#                             min_idx = j
#                         break
#                     elif tmp_cop <= 0:
#                         if min_v > tmp_v:
#                             min_v = tmp_v
#                         elif min_v == tmp_v and (min_idx == -1 or possibles[min_idx][0] <= possibles[j][0]):
#                             min_idx = j
#                         break
#                 print(3, min_v, possibles[j], problems[i])
                
#     return (alp+(possibles[min_idx][0]*(min_v // possibles[min_idx][2])), cop+(possibles[min_idx][1]*(min_v // possibles[min_idx][2])), answer+min_v)

# def divide(possible):
#     d_alp = possible[0] // possible[2] if possible[0] % possible[2] == 0 else possible[0] // possible[2] + 1
#     d_cop = possible[1] // possible[2] if possible[1] % possible[2] == 0 else possible[1] // possible[2] + 1
#     # cnt_alp = alp // d_alp if alp % d_alp == 0 else alp // d_alp + 1
#     # cnt_cop = cop // d_cop if cop % d_cop == 0 else cop // d_cop + 1
#     return d_alp, d_cop

solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
print()
solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])