def solution(str1, str2):
    M = 65536                                                         # 출력 시 자카드 유사도에 곱해줄 실수
    str1, str2 = str1.upper(), str2.upper()                           # 문자열 대문자로 변환하여 저장
    list1, list2 = [], []                                             # 다중집합 리스트 생성
    
    for idx in range(len(str1)-1):                                    # 문자열을 순회하면서 두 글자 모두 알파벳이면 리스트에 추가
        if str1[idx].isalpha() and str1[idx+1].isalpha():
            list1.append(str1[idx]+str1[idx+1])
    for idx in range(len(str2)-1):
        if str2[idx].isalpha() and str2[idx+1].isalpha():
            list2.append(str2[idx]+str2[idx+1])

    idx = 0
    kyo = 0                                                           # 교집합의 길이를 담을 변수 생성
    if len(list1 + list2) != 0:                                       # 두 다중집합이 모두 공집합이 아니면
        while idx < len(list1):                                       # list1을 순회하며
            target = list1[idx]
            if target in list2:                                       # list1의 원소가 list2에 있다면
                kyo += 1                                              # 교집합의 길이 += 1
                list1.remove(target)                                  # 다중집합에서 해당 원소 제거
                list2.remove(target)
            else:                                                     # list1의 원소가 list2에 없다면
                idx += 1                                              # idx += 1
    
        hap = kyo + len(list1+ list2)                                 # 합집합의 길이 == 교집합의 길이 + (list1 + list2)의 길이
        jq = int(kyo / hap)                                           # 자카드 유사도
        return jq * M
    else:
        return M