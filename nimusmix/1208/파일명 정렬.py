from collections import defaultdict

def solution(files):
    info = defaultdict(dict)                                         # {head: {number: file}} 형태로 담을 딕셔너리
    
    for file in files:
        for idx, i in enumerate(file):
            if i.isdigit():                                           # 첫 번째로 나오는 숫자 찾기
                head = file[0:idx].upper()                            # head에 첫 번째 숫자 이전까지를 대문자로 저장
                
                for j in range(idx, idx+5):                           # number는 최대 5글자이므로 첫 번째 숫자부터 5회 순회
                    if j < len(file) and not file[j].isdigit():       # 숫자가 아니면 tail이므로
                        number = int(file[idx:j])                     # 그 전까지 number에 저장
                        break
                else:
                    number = int(file[idx:idx+5])                     # 5글자까지 모두 숫자이면 그대로 number에 저장
                
                if number in info[head]:                              # info[head][number]에 파일명 저장
                    info[head][number] += [file]
                else:
                    info[head][number] = [file]
                    
                break                                                 # 첫 번째 숫자만 찾으면 되므로 바로 break
            
    ans = []
    for h in sorted(info.keys()):                                     # sorted(info.keys()) = 정렬된 heads
        for n in (sorted(info[h].keys())):                            # sorted(info[h].keys()) = 정렬된 numbers
            ans += info[h][n]                                         # info[h][n] = 같은 head, 같은 number인 파일 리스트
            
    return ans


# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (1.93ms, 10.6MB)
# 테스트 4 〉	통과 (1.97ms, 10.5MB)
# 테스트 5 〉	통과 (1.86ms, 10.6MB)
# 테스트 6 〉	통과 (1.87ms, 10.5MB)
# 테스트 7 〉	통과 (1.84ms, 10.4MB)
# 테스트 8 〉	통과 (1.66ms, 10.4MB)
# 테스트 9 〉	통과 (1.74ms, 10.5MB)
# 테스트 10 〉	통과 (1.84ms, 10.4MB)
# 테스트 11 〉	통과 (1.79ms, 10.3MB)
# 테스트 12 〉	통과 (1.85ms, 10.4MB)
# 테스트 13 〉	통과 (1.81ms, 10.6MB)
# 테스트 14 〉	통과 (1.98ms, 10.3MB)
# 테스트 15 〉	통과 (1.88ms, 10.4MB)
# 테스트 16 〉	통과 (1.66ms, 10.4MB)
# 테스트 17 〉	통과 (1.67ms, 10.5MB)
# 테스트 18 〉	통과 (1.78ms, 10.3MB)
# 테스트 19 〉	통과 (1.81ms, 10.4MB)
# 테스트 20 〉	통과 (2.06ms, 10.4MB)