from collections import deque
def solution(s):
    N = len(s)      #s길이
    i = 0           #index
    count = 1    #개수로 뽑아냄
    edits = []   #수정된 리스트 전부받음
    len_li = []  #길이 검출을 위함2
    while True:
        edits.append(s[i:i + count])
        i = i + count
        if i + count > N:
            #print(edits)
            len_edit = N  #edit 길이 검출을 위함
            continu = 0
            for idx in range(1, len(edits)):      # 압축
                if edits[idx - 1] == edits[idx]:  # 숫자 붙이기  
                    len_edit -= len(edits[idx]) 
                    if continu > 1:               
                        continu += 1
                        if continu == 10:        #자릿수 검증
                            len_edit += 1
                        elif continu == 100:
                            len_edit += 1
                        elif continu == 1000:
                            len_edit += 1
                    elif continu == 0:
                        continu += 2
                        len_edit += 1
                else:
                    continu = 0
            #print(len_edit)
            #초기화 구문
            len_li.append(len_edit)
            #print(len_li)
            i = 0
            count += 1
            len_edit = N
            continu = 0
            edits.clear()
            
        # count가 N보다 클 필요는 없어 제외
        if count > N // 2:
            break
    
    answer = min(len_li)
    return answer


# 테스트 1 〉	통과 (0.03ms, 10.1MB)
# 테스트 2 〉	통과 (0.35ms, 10.2MB)
# 테스트 3 〉	통과 (0.32ms, 10.2MB)
# 테스트 4 〉	통과 (0.04ms, 10.4MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.07ms, 10.2MB)
# 테스트 7 〉	통과 (0.37ms, 10.2MB)
# 테스트 8 〉	통과 (0.39ms, 10.3MB)
# 테스트 9 〉	통과 (0.54ms, 10.2MB)
# 테스트 10 〉	통과 (2.07ms, 10.2MB)
# 테스트 11 〉	통과 (0.14ms, 10.1MB)
# 테스트 12 〉	통과 (0.08ms, 10.2MB)
# 테스트 13 〉	통과 (0.10ms, 10.4MB)
# 테스트 14 〉	통과 (0.90ms, 10.2MB)
# 테스트 15 〉	통과 (0.09ms, 10MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (1.45ms, 10.2MB)
# 테스트 18 〉	통과 (1.60ms, 10.2MB)
# 테스트 19 〉	통과 (0.89ms, 10.2MB)
# 테스트 20 〉	통과 (2.19ms, 10.3MB)
# 테스트 21 〉	통과 (2.09ms, 10.2MB)
# 테스트 22 〉	통과 (2.05ms, 10.1MB)
# 테스트 23 〉	통과 (1.97ms, 10.3MB)
# 테스트 24 〉	통과 (1.86ms, 10.2MB)
# 테스트 25 〉	통과 (2.01ms, 10.2MB)
# 테스트 26 〉	통과 (2.00ms, 10.2MB)
# 테스트 27 〉	통과 (2.30ms, 10.1MB)
# 테스트 28 〉	통과 (0.02ms, 10.2MB)