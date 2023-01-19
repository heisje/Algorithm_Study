def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(i * str(N)))            # N을 i만큼 붙여서 쓸 때

        for j in range(i-1):
            for x in dp[j]:
                for y in dp[i-j-2]:
                    numbers.add(x + y)
                    numbers.add(x * y)
                    numbers.add(x - y)
                    if y != 0:
                        numbers.add(x // y)
        if number in numbers:
            return i

        dp.append(numbers)

    return answer

'''
테스트 1 〉	통과 (0.69ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (16.84ms, 11.1MB)
테스트 5 〉	통과 (10.96ms, 11.1MB)
테스트 6 〉	통과 (0.17ms, 10.1MB)
테스트 7 〉	통과 (0.26ms, 10.3MB)
테스트 8 〉	통과 (15.24ms, 11.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
'''