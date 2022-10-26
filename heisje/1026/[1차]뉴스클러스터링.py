import re
p = re.compile('[A-Z][A-Z]')
from collections import defaultdict
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    arr1 = []
    arr2 = [] 
    for i in range(0, len(str1)-1):
        temp = str1[i:i+2]
        m = p.match(temp)
        if m:
            arr1.append(temp)
    for i in range(0, len(str2)-1):
        temp = str2[i:i+2]
        m = p.match(temp)
        if m:
            arr2.append(temp)
    # print(arr1)
    # print(arr2)
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    for a in arr1:
        dict1[a] += 1
    for a in arr2:
        dict2[a] += 1

    #합집합은 dict들을 순회하면서, 큰 수를 찾는다.
    dict_u = defaultdict(int)
    for key, value in dict1.items():
        dict_u[key] = value

    for key, value in dict2.items():
        if dict_u[key]:  # 만약 들어있으면
            if dict2[key] > dict1[key]:  # 비교를 해서
                dict_u[key] = dict2[key]
            else: 
                dict_u[key] = dict1[key]
        else:
            dict_u[key] = dict2[key]

    #교집합은 dict들을 순회하면서, 작은 수를 찾는다.
    dict_n = defaultdict(int)
    for key, value in dict1.items():
        if key in dict2:
            if dict1[key] > dict2[key]:
                dict_n[key] = dict2[key]
            else:
                dict_n[key] = dict1[key]
    # print(dict_n)
    # print(dict_u)
    dict_u_sum_vlues = 0
    for value in dict_u.values():
        dict_u_sum_vlues += value

    dict_n_sum_vlues = 0
    for value in dict_n.values():
        dict_n_sum_vlues += value

    if dict_u_sum_vlues == 0:
        answer = 65536
    else:
        answer = int(dict_n_sum_vlues / dict_u_sum_vlues * 65536)
    return answer

# LV2 / 40분

# 실행결과
# print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
# print(solution('aa1+aa2','AAAA12'))
# print(solution('E=M*C^2','e=m*c^2'))
# print(solution("di mi mi mi mi","di di di go"))
# print(solution("BAAAA","AAA"))
