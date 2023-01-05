def makeSet(String):
    arr = []
    for i in range(len(String)-1):
        if 'A' <= String[i] <= 'Z' and 'A' <= String[i+1] <= 'Z':
            arr.append((String[i] + String[i+1]))
    return arr

def solution(str1, str2):
    set1 = makeSet(str1.upper())    # 모두 다 대문자로 변환
    set2 = makeSet(str2.upper())

    # # 합집합 구하기
    # tmp = set1[:]                   # set1 copy array 생성
    # union = len(set1)               # 합집합 개수 set1의 개수로 초기화
    # for i in set2:                  # set2 돌면서
    #     if i not in tmp:            # set1에 없으면
    #         union += 1              # 합집합 +1
    #     else:                       # set1에 있으면
    #         tmp.remove(i)           # tmp 에서 해당 원소 제거

    # 교집합 구하기
    tmp = set1[:]                   # set1 copy array 생성
    intersection = 0                # 교집합 개수 0으로 설정
    for i in set2:                  # set2 돌면서
        if i in tmp:                # set1에 있으면
            intersection += 1       # 교집합 +1
            tmp.remove(i)           # tmp 에서 제거

    union = len(set1) + len(set2) - intersection
    answer = int(intersection/union * 65536) if union else 65536
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))