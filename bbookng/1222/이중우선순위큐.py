import heapq

def solution(operations):
    answer = []

    for operation in operations:
        order, number = operation.split()

        # 큐에 주어진 숫자 삽입
        if order == 'I':
            heapq.heappush(answer, int(number)) # 최소힙 활용을 위해 힙큐 사용

        # 큐에서 number에 따라 최소, 최댓값 삭제
        else:
            if not answer:                  # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우,
                continue                    # 해당 연산 무시
            if number == '1':               # D 1 일 경우,
                answer.remove(max(answer))  # 현재 큐에서 최댓값 삭제
            else:                           # D -1 일 경우,
                heapq.heappop(answer)       # 최소힙을 이용하여 최솟값 삭제

    if not answer:      # 큐가 비어있으면
        return [0, 0]
    else:
        return [max(answer), min(answer)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

'''
테스트 1 〉	통과 (0.08ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
'''