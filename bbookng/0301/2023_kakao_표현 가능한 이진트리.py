def fill_number(number):
    tmp = 0
    while True:
        if 2 ** tmp - 1 >= len(bin(number)[2:]):
            break
        tmp += 1
    return tmp

def check(number, p):
    mid = len(number) // 2

    if not p:
        if '1' in number:
            return False

    if len(number) == 1:
        return number

    return check(number[mid+1:], int(number[mid])) and check(number[:mid], int(number[mid]))


def solution(numbers):
    answer = []
    for number in numbers:
        number = bin(number)[2:].zfill(2**fill_number(number)-1)
        answer.append(1 if check(number, int(number[len(number)//2])) else 0)
    return answer

print(solution([7, 42, 5]))
print(solution([63, 111, 95]))

'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (0.24ms, 10.3MB)
테스트 5 〉	통과 (0.50ms, 10.3MB)
테스트 6 〉	통과 (0.85ms, 10.1MB)
테스트 7 〉	통과 (1.32ms, 10.3MB)
테스트 8 〉	통과 (0.67ms, 10.3MB)
테스트 9 〉	통과 (6.69ms, 10.4MB)
테스트 10 〉	통과 (53.26ms, 11.1MB)
테스트 11 〉	통과 (60.08ms, 11.5MB)
테스트 12 〉	통과 (59.92ms, 11.2MB)
테스트 13 〉	통과 (54.97ms, 11.2MB)
테스트 14 〉	통과 (52.79ms, 11.1MB)
테스트 15 〉	통과 (36.10ms, 10.8MB)
테스트 16 〉	통과 (97.10ms, 11.5MB)
테스트 17 〉	통과 (103.04ms, 11.3MB)
테스트 18 〉	통과 (97.74ms, 11.1MB)
테스트 19 〉	통과 (80.28ms, 11.2MB)
테스트 20 〉	통과 (51.45ms, 10.6MB)
'''