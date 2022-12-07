from itertools import combinations

def solution(orders, course):
    info = {}
    ans = []
    
    for order in orders:
        for i in order:
            info[i] = 1

    for num in course:
        max_cnt = 0
        tmp = []
        
        for combi in combinations(info, num):
            cnt = 0
            
            for order in orders:
                for i in combi:
                    if i not in order:
                        break
                else:
                    cnt += 1

            if cnt > 1:
                max_cnt = max(max_cnt, cnt)
                if max_cnt > 1 and max_cnt == cnt:
                    tmp.append((cnt, ''.join(combi)))
                    
        for i in tmp:
            if i[0] == max_cnt:
                ans.append(i[1])

    ans.sort()
    return ans



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))