from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount_list = [[10, 20, 30, 40] for _ in range(len(emoticons))]
    
    for discounts in product(*discount_list):
        tmp = [0, 0]
        for user in users:
            price = 0
            for i in range(len(emoticons)):
                if user[0] <= discounts[i]:
                    price += (100 - discounts[i]) * 0.01 * emoticons[i]
            
            if price >= user[1]:
                tmp[0] += 1
            else:
                tmp[1] += price
                
        if tmp[0] > answer[0]:
            answer = [tmp[0], int(tmp[1])]
        elif tmp[0] == answer[0] and tmp[1] > answer[1]:
            answer[1] = int(tmp[1])
            
    return answer

'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (0.87ms, 10.3MB)
테스트 4 〉	통과 (2.22ms, 10.3MB)
테스트 5 〉	통과 (4.38ms, 10.2MB)
테스트 6 〉	통과 (2.11ms, 10.2MB)
테스트 7 〉	통과 (21.10ms, 10.2MB)
테스트 8 〉	통과 (9.96ms, 10.3MB)
테스트 9 〉	통과 (99.43ms, 10.2MB)
테스트 10 〉	통과 (42.76ms, 10.2MB)
테스트 11 〉	통과 (462.67ms, 10.3MB)
테스트 12 〉	통과 (213.43ms, 10.4MB)
테스트 13 〉	통과 (2049.85ms, 10.2MB)
테스트 14 〉	통과 (2002.87ms, 10.3MB)
테스트 15 〉	통과 (94.39ms, 10.3MB)
테스트 16 〉	통과 (94.86ms, 10.4MB)
테스트 17 〉	통과 (0.45ms, 10.4MB)
테스트 18 〉	통과 (28.97ms, 10.3MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.06ms, 10.4MB)
'''