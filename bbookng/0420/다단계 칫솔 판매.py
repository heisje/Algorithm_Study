def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll) + 1)
    dic = dict()
    root = [i for i in range(len(enroll)+1)]

    for i in range(len(enroll)):
        dic[enroll[i]] = i + 1

    for i in range(len(enroll)):
        if referral[i] == '-':
            root[i+1] = 0
        else:
            root[i+1] = dic[referral[i]]

    for i in range(len(seller)):
        profit = amount[i] * 100
        person = dic[seller[i]]

        while True:
            # 절사할 금액이 없으면 위로 더 안올라가고 바로 멈추기
            # center면 멈추기
            if profit < 10 or root[person] == person:
                answer[person] += profit
                break
            bonus = profit // 10
            answer[person] += profit - bonus
            profit = bonus
            person = root[person]

    return answer[1:]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))

'''테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.1MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (0.74ms, 10.2MB)
테스트 6 〉	통과 (3.99ms, 12.9MB)
테스트 7 〉	통과 (4.60ms, 12.9MB)
테스트 8 〉	통과 (8.46ms, 12.9MB)
테스트 9 〉	통과 (14.10ms, 13.7MB)
테스트 10 〉	통과 (84.82ms, 20.9MB)
테스트 11 〉	통과 (80.19ms, 20.5MB)
테스트 12 〉	통과 (77.95ms, 20.6MB)
테스트 13 〉	통과 (77.06ms, 20.6MB)
'''