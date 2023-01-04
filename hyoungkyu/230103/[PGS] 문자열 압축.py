# Lv2
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):         # 문자열의 절반까지만 확인하면 됨
        change = ''                         # 단위마다 자른 문자열
        tmp = ''                            # 임시 변수
        cnt = 1                             # 반복 횟수
        for j in range(0, len(s)-i+1, i):   # 단위마다 간격을 둬서 진행
            
            if tmp == s[j:j+i]:             # 뒤의 값이 앞의 값과 같으면
                cnt += 1                    # count 증가
            
            else:                           # 뒤의 값이 앞의 값과 다르면
                change += str(cnt) + tmp if cnt!=1 else tmp # 숫자와 함께 앞의 값을 기록
                tmp = s[j:j+i]              # 임시 변수 재할당
                cnt = 1                     # count 초기화
                
            if j == len(s)-i:               # 단위로 딱 나누어 떨어질 때 마지막 값 처리
                change += str(cnt) + tmp if cnt!=1 else tmp
                
        if len(s)%i:                        # 단위로 안나누어 떨어질 때 마지막 값 처리
            change += str(cnt) + s[len(s)-i-(len(s)%i):] if cnt != 1 else s[len(s)-i-(len(s)%i):]
        
        answer = min(answer, len(change))   # 최소값 갱신
        # if change: print(i, change, len(change))
        
            
    return answer

'''
테스트 1 〉통과 (0.03ms, 10.4MB)
테스트 2 〉통과 (0.39ms, 10.3MB)
테스트 3 〉통과 (0.20ms, 10.2MB)
테스트 4 〉통과 (0.03ms, 10.2MB)
테스트 5 〉통과 (0.00ms, 10.4MB)
테스트 6 〉통과 (0.04ms, 10.2MB)
테스트 7 〉통과 (0.47ms, 10.2MB)
테스트 8 〉통과 (0.45ms, 10.3MB)
테스트 9 〉통과 (0.71ms, 10.3MB)
테스트 10 〉통과 (2.66ms, 10.2MB)
테스트 11 〉통과 (0.10ms, 10.4MB)
테스트 12 〉통과 (0.10ms, 10.2MB)
테스트 13 〉통과 (0.11ms, 10.4MB)
테스트 14 〉통과 (0.71ms, 10.4MB)
테스트 15 〉통과 (0.11ms, 10.3MB)
테스트 16 〉통과 (0.02ms, 10.1MB)
테스트 17 〉통과 (1.29ms, 10.3MB)
테스트 18 〉통과 (1.30ms, 10.2MB)
테스트 19 〉통과 (1.52ms, 10.1MB)
테스트 20 〉통과 (3.22ms, 10.4MB)
테스트 21 〉통과 (2.86ms, 10.1MB)
테스트 22 〉통과 (2.88ms, 10.1MB)
테스트 23 〉통과 (3.09ms, 10.3MB)
테스트 24 〉통과 (2.69ms, 10.2MB)
테스트 25 〉통과 (2.95ms, 10.4MB)
테스트 26 〉통과 (3.42ms, 10.3MB)
테스트 27 〉통과 (5.17ms, 10.4MB)
테스트 28 〉통과 (0.03ms, 10.1MB)
'''