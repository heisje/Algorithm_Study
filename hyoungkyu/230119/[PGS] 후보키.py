# Lv3
from itertools import combinations

def solution(relation):
    answer = 0
    idxs = [i for i in range(len(relation[0]))]
    result_lst = []
    
    # 유일성 구하기
    for i in range(1, len(idxs)+1):
        for combination in combinations(idxs, i):
            tmp_dic = {}  
            for a in relation:
                tmp_str = ""
                for idx in combination:
                    tmp_str += a[idx]
                if tmp_str not in tmp_dic:
                    tmp_dic[tmp_str] = 1
                else:
                    break
            else:
                tmp_str = ""
                for j in combination:
                    tmp_str += str(j)
                result_lst.append(tmp_str)
    
    # 최소성 구하기
    res = []
    for i in result_lst:
        if not res:
            res.append(i)
            answer += 1
            continue
        for j in res:
            for k in j:
                if k not in i:
                    break
            else:
                break
        else:
            res.append(i)
            answer += 1   
    return answer

'''
테스트 1 〉통과 (0.03ms, 10.4MB)
테스트 2 〉통과 (0.05ms, 10.3MB)
테스트 3 〉통과 (0.03ms, 10.3MB)
테스트 4 〉통과 (0.03ms, 10.2MB)
테스트 5 〉통과 (0.02ms, 10.2MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.01ms, 10.1MB)
테스트 8 〉통과 (0.02ms, 10.2MB)
테스트 9 〉통과 (0.10ms, 10.4MB)
테스트 10 〉통과 (0.08ms, 10.2MB)
테스트 11 〉통과 (0.23ms, 10.1MB)
테스트 12 〉통과 (0.61ms, 10.3MB)
테스트 13 〉통과 (0.19ms, 10.4MB)
테스트 14 〉통과 (0.03ms, 10.2MB)
테스트 15 〉통과 (0.03ms, 10.4MB)
테스트 16 〉통과 (0.04ms, 10.2MB)
테스트 17 〉통과 (0.05ms, 10.3MB)
테스트 18 〉통과 (2.39ms, 10.3MB)
테스트 19 〉통과 (1.13ms, 10.2MB)
테스트 20 〉통과 (4.03ms, 10.2MB)   *
테스트 21 〉통과 (0.66ms, 10.1MB)
테스트 22 〉통과 (0.89ms, 10.2MB)
테스트 23 〉통과 (0.06ms, 10.4MB)
테스트 24 〉통과 (0.99ms, 10.3MB)
테스트 25 〉통과 (3.50ms, 10.2MB)
테스트 26 〉통과 (2.03ms, 10.2MB)
테스트 27 〉통과 (0.36ms, 10.3MB)
테스트 28 〉통과 (0.15ms, 10.1MB)
'''