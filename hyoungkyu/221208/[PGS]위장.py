# from itertools import combinations 

def solution(clothes):
    answer = 1
    dic = {}
    for cloth, kind in clothes:
        if kind not in dic:
            dic[kind] = []
        dic[kind].append(cloth)
    cnt_lst = [0] * len(dic)
    i = 0
    for key in dic.keys():
        cnt_lst[i] =len(dic[key])
        i += 1
    
    for num in cnt_lst:
        answer *= (num+1)       # 안입는 경우도 각 케이스에 포함시킨 후 다 곱하고, 마지막에 다 안입는 경우만 빼주면 됨
    return answer-1
    
    # for i in range(1, len(cnt_lst)+1):
    #     for j in combinations(cnt_lst, i):
    #         tmp = 0
    #         for k in j:
    #             if not tmp:
    #                 tmp = k
    #             else:
    #                 tmp *= k
    #         answer += tmp
        
    # def comb(n):
    #     lst = []
    #     tot = 0
    #     for i in range(0, 1<<n):
    #         tmp = []
    #         for j in range(0, n):
    #             if i & (1<<j):
    #                 tmp.append(cnt_lst[j])
    #         lst.append(tmp[:])
    #     for i in lst:
    #         tmp = 0
    #         for num in i:
    #             if not tmp:
    #                 tmp = num
    #             else:
    #                 tmp *= num
    #         tot += tmp
    #     return tot
    # answer = comb(len(cnt_lst))
    
    # return answer

'''
테스트 1 〉통과 (0.02ms, 10.2MB)
테스트 2 〉통과 (0.01ms, 10.4MB)
테스트 3 〉통과 (0.01ms, 10.4MB)
테스트 4 〉통과 (0.02ms, 10.2MB)
테스트 5 〉통과 (0.01ms, 10.2MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.02ms, 10.2MB)
테스트 8 〉통과 (0.01ms, 10.2MB)
테스트 9 〉통과 (0.01ms, 10.2MB)
테스트 10 〉통과 (0.01ms, 10.3MB)
테스트 11 〉통과 (0.01ms, 10.2MB)
테스트 12 〉통과 (0.01ms, 10.2MB)
테스트 13 〉통과 (0.01ms, 10.1MB)
테스트 14 〉통과 (0.01ms, 10.3MB)
테스트 15 〉통과 (0.01ms, 10.2MB)
테스트 16 〉통과 (0.00ms, 10.3MB)
테스트 17 〉통과 (0.01ms, 10.2MB)
테스트 18 〉통과 (0.01ms, 10.2MB)
테스트 19 〉통과 (0.02ms, 10.2MB)
테스트 20 〉통과 (0.01ms, 10.2MB)
테스트 21 〉통과 (0.01ms, 10.2MB)
테스트 22 〉통과 (0.01ms, 10.4MB)
테스트 23 〉통과 (0.01ms, 10.2MB)
테스트 24 〉통과 (0.01ms, 10.2MB)
테스트 25 〉통과 (0.01ms, 10.3MB)
테스트 26 〉통과 (0.01ms, 10.4MB)
테스트 27 〉통과 (0.01ms, 10.3MB)
테스트 28 〉통과 (0.01ms, 10.3MB)
'''