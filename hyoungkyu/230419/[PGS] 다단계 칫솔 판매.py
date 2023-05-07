def sell(tot):
    bbing = int(tot * 0.1)
    return (tot-bbing, bbing)

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    dic = {}
    for i in range(len(enroll)):
        dic[enroll[i]] = i
    for i in range(len(seller)):
        idx = dic[seller[i]]                    # 판매원이 누구냐
        tot = amount[i] * 100                   # 판매액
        
        while True:
            yangachi = referral[idx]            # 나를 다단계로 꼬신놈
            my_money, bbing = sell(tot)         # 돈 계산
            answer[idx] += my_money             # 내 돈 챙기자
            tot = bbing                         # 삥 뜯긴걸로 갱신
            if yangachi == "-" or tot < 1: break    # 종료 조건
            idx = dic[yangachi]                 # 다음 희생자 계산
            
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.11ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.4MB)
테스트 5 〉	통과 (1.26ms, 10.5MB)
테스트 6 〉	통과 (1.43ms, 12.4MB)
테스트 7 〉	통과 (1.67ms, 12.5MB)
테스트 8 〉	통과 (3.55ms, 12.6MB)
테스트 9 〉	통과 (32.41ms, 13.3MB)
    테스트 10 〉	통과 (196.87ms, 20.8MB)
테스트 11 〉	통과 (140.15ms, 20.4MB)
테스트 12 〉	통과 (179.98ms, 20.5MB)
테스트 13 〉	통과 (168.69ms, 20.4MB)
'''