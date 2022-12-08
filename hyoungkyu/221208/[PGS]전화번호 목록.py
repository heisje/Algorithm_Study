def solution(phone_book):
    # answer = True
    # for num1 in phone_book:
    #     for num2 in phone_book:
    #         if num2 == num1:
    #             continue
    #         if num2[:len(num1)] == num1:
    #             answer = False
    #             return answer
    # return answer
    
    answer = True
    dic = {}
    for num in phone_book:
        dic[num] = 1
        
    for num in phone_book:
        tmp = ''
        for i in range(len(num)-1):
            tmp += num[i]
            if tmp in dic:
                answer = False
                return answer
    return answer

'''
정확성 테스트
테스트 1 〉통과 (0.01ms, 10.1MB)
테스트 2 〉통과 (0.00ms, 10.1MB)
테스트 3 〉통과 (0.00ms, 10.1MB)
테스트 4 〉통과 (0.00ms, 10.3MB)
테스트 5 〉통과 (0.00ms, 10.2MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.00ms, 10.1MB)
테스트 8 〉통과 (0.00ms, 10.1MB)
테스트 9 〉통과 (0.00ms, 9.98MB)
테스트 10 〉통과 (0.00ms, 10.2MB)
테스트 11 〉통과 (0.01ms, 10.1MB)
테스트 12 〉통과 (0.00ms, 10.3MB)
테스트 13 〉통과 (0.00ms, 10MB)
테스트 14 〉통과 (115.99ms, 10.2MB)
테스트 15 〉통과 (96.91ms, 10.3MB)
테스트 16 〉통과 (307.47ms, 10.5MB)
테스트 17 〉통과 (464.24ms, 10.5MB)
테스트 18 〉통과 (609.07ms, 10.4MB)
테스트 19 〉통과 (710.92ms, 10.4MB)
테스트 20 〉통과 (1012.09ms, 10.4MB)
효율성  테스트
테스트 1 〉통과 (1.11ms, 10.8MB)
테스트 2 〉통과 (1.26ms, 10.8MB)
테스트 3 〉실패 (시간 초과)
테스트 4 〉실패 (시간 초과)
'''

'''
정확성  테스트
테스트 1 〉통과 (0.01ms, 10.1MB)
테스트 2 〉통과 (0.01ms, 10.3MB)
테스트 3 〉통과 (0.01ms, 10.2MB)
테스트 4 〉통과 (0.01ms, 10.1MB)
테스트 5 〉통과 (0.01ms, 10.2MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.01ms, 10.2MB)
테스트 8 〉통과 (0.00ms, 10.1MB)
테스트 9 〉통과 (0.00ms, 10.2MB)
테스트 10 〉통과 (0.01ms, 10.1MB)
테스트 11 〉통과 (0.01ms, 10.2MB)
테스트 12 〉통과 (0.01ms, 10.1MB)
테스트 13 〉통과 (0.01ms, 10.3MB)
테스트 14 〉통과 (1.35ms, 10.3MB)
테스트 15 〉통과 (2.09ms, 10.5MB)
테스트 16 〉통과 (4.15ms, 10.4MB)
테스트 17 〉통과 (5.44ms, 10.4MB)
테스트 18 〉통과 (7.07ms, 10.4MB)
테스트 19 〉통과 (2.65ms, 10.5MB)
테스트 20 〉통과 (5.80ms, 10.6MB)
효율성  테스트
테스트 1 〉통과 (1.13ms, 11.3MB)
테스트 2 〉통과 (1.22ms, 11.3MB)
테스트 3 〉통과 (492.58ms, 46.8MB)
테스트 4 〉통과 (218.43ms, 34.5MB)
'''
