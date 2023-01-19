# Lv3
from collections import defaultdict

def binary_search(lst, tar):
    s = 0
    e = len(lst) - 1
    while s <= e:
        mid = (s+e) // 2
        if lst[mid] < tar:
            s = mid+1
        else:
            e = mid-1
    return s

def solution(info, query):
    # 언어, 직군, 경력, 소울푸드, 점수
    lst = [("-", "cpp", "java", "python"),
          ("-", "backend", "frontend"),
          ("-", "junior", "senior"),
          ("-", "chicken", "pizza")]
    answer = []
    
    # info, query 리스트화
    infos = [list(i.split()) for i in info]
    querys = []
    for q in query:
        tmp_lst = []
        for i in q.split():
            if i == "and":
                continue
            tmp_lst.append(i)
        querys.append(tmp_lst)
    
    # 각 조건별로 분류해놓기
    dic = defaultdict(list)
    for i in lst[0]:
        for j in lst[1]:
            for k in lst[2]:
                for m in lst[3]:
                    for info in infos:
                        if (i == "-" or i == info[0]) and (j == "-" or j == info[1]) and (k == "-" or k == info[2]) and (m == "-" or m == info[3]):
                            dic[i+j+k+m].append(int(info[4]))
    
    # dic 정렬
    for key in dic.keys():
        dic[key].sort()
    # print(dic)
    # query별 만족 인스턴스 개수 구하기
    for query in querys:
        cnt = 0
        s = "".join(query[:4])
            
        # ** 이진탐색으로 개수 찾는 방법 적용하기 **
        idx = binary_search(dic[s], int(query[4]))
        
        answer.append(len(dic[s])-idx)
    return answer

'''
정확성  테스트
테스트 1 〉통과 (0.39ms, 10.4MB)
테스트 2 〉통과 (0.39ms, 10.5MB)
테스트 3 〉통과 (0.54ms, 10.4MB)
테스트 4 〉통과 (2.14ms, 10.6MB)
테스트 5 〉통과 (3.64ms, 10.6MB)
테스트 6 〉통과 (9.16ms, 10.7MB)
테스트 7 〉통과 (4.56ms, 11MB)
테스트 8 〉통과 (86.74ms, 13.3MB)
테스트 9 〉통과 (87.82ms, 15.2MB)
테스트 10 〉통과 (90.06ms, 15.7MB)  *
테스트 11 〉통과 (3.67ms, 10.8MB)
테스트 12 〉통과 (9.31ms, 10.8MB)
테스트 13 〉통과 (4.86ms, 11.1MB)
테스트 14 〉통과 (43.03ms, 13.2MB)
테스트 15 〉통과 (43.27ms, 13.2MB)
테스트 16 〉통과 (3.62ms, 10.7MB)
테스트 17 〉통과 (9.44ms, 10.9MB)
테스트 18 〉통과 (43.29ms, 13.2MB)
효율성  테스트
테스트 1 〉통과 (1411.74ms, 115MB)
테스트 2 〉통과 (1270.33ms, 115MB)
테스트 3 〉통과 (1414.85ms, 101MB)  *
테스트 4 〉통과 (1397.14ms, 102MB)
'''