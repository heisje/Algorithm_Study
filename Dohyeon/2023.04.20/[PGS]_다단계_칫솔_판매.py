import math

class Member:

    parent = None
    money = 0

    def __init__(self, name):
        self.name = name

    def getParent(self):
        return self.parent

    def getMoney(self):
        return self.money

def moneyDistribution(memberDict, name, money):
    MyParent = memberDict[name].parent
    if MyParent == "-":
        if money * 0.1 < 1:
            temp = 0
        else:
            temp = math.floor(money * 0.1)
        memberDict[name].money += money - temp
    else:
        while(True):
            if money * 0.1 < 1:
                temp = 0
            else:
                temp = math.floor(money * 0.1)
            memberDict[name].money += money - temp
            if MyParent == "-":
                break
            money = temp
            name = memberDict[name].parent
            MyParent = memberDict[name].parent

def solution(enroll, referral, seller, amount):
    answer = []
    member_dict = {}

    for i in range(len(enroll)):
        new_member = Member(enroll[i])          # 클래스 생성
        new_member.parent = referral[i]         # 부모 설정
        member_dict[enroll[i]] = new_member


    for i in range(len(seller)):
        moneyDistribution(member_dict, seller[i], amount[i]*100)

    for i in range(len(enroll)):
        answer.append(member_dict[enroll[i]].money)

    return answer


"""
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.13ms, 10.3MB)
테스트 3 〉	통과 (0.13ms, 10.2MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (3.54ms, 10.5MB)
테스트 6 〉	통과 (6.91ms, 13.6MB)
테스트 7 〉	통과 (7.84ms, 13.5MB)
테스트 8 〉	통과 (18.62ms, 13.7MB)
테스트 9 〉	통과 (65.41ms, 14.7MB)
테스트 10 〉	통과 (380.41ms, 21.5MB)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
"""