def solution(phone_book):
    hash = dict()

    for number in phone_book:
        hash[number] = 1

    for number in phone_book:
        check = ''
        for num in number:
            check += num
            if check in hash and check != number:
                return False

    return True

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (1.15ms, 10.2MB)
테스트 15 〉	통과 (1.57ms, 10.3MB)
테스트 16 〉	통과 (6.07ms, 10.3MB)
테스트 17 〉	통과 (6.12ms, 10.4MB)
테스트 18 〉	통과 (6.63ms, 10.3MB)
테스트 19 〉	통과 (3.19ms, 10.4MB)
테스트 20 〉	통과 (4.16ms, 10.5MB)

효율성  테스트
테스트 1 〉	통과 (1.07ms, 11.3MB)
테스트 2 〉	통과 (1.15ms, 11.4MB)
테스트 3 〉	통과 (458.97ms, 46.7MB)
테스트 4 〉	통과 (176.70ms, 34.7MB)
'''