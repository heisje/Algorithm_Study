# [x, y, a, b]
# x, y : 기둥, 보를 설치 또는 삭제할 교차점의 좌표
# a : 구조물의 종류, 0 : 기둥, 1 : 보
# b : 삭제 또는 설치 0 : 삭제, 1 : 설치

# return 시 x, y 좌표가 같은 경우는 기둥이 보보다 앞에 오면 됨.
# [x, y, a] 형태, x좌표 기준으로 오름차순 > y좌표 기준으로 오름차순

def solution(n, build_frame):
    answer = []

    for build in build_frame:
        x, y, a, b = build

        if a == 0 and b == 1:
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                answer.append([x, y, a])

        elif a == 0 and b == 0 and [x, y, a] in answer:
            answer.remove([x, y, a])
            if y != 0 and [x, y-1, 0] not in answer and [x-1, y, 1] not in answer and [x, y, 1] not in answer:
                answer.append([x, y, a])

        elif a == 1 and b == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                answer.append([x, y, a])

        elif a == 1 and b == 0 and [x, y, a] in answer:
            answer.remove([x, y, a])
            if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer and ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                answer.append([x, y, a])

        answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

# chatGPT 가 짜준 코드
def is_valid(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥인 경우
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
        else:  # 보인 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치하는 경우
            answer.append([x, y, a])
            if not is_valid(answer):
                answer.remove([x, y, a])
        else:  # 삭제하는 경우
            answer.remove([x, y, a])
            if not is_valid(answer):
                answer.append([x, y, a])
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

'''
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.1MB)
테스트 3 〉	통과 (0.08ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.3MB)
테스트 5 〉	통과 (0.27ms, 10.2MB)
테스트 6 〉	통과 (0.52ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (343.43ms, 10.5MB)
테스트 11 〉	통과 (2206.48ms, 10.4MB)
테스트 12 〉	통과 (200.54ms, 10.3MB)
테스트 13 〉	통과 (1990.39ms, 10.5MB)
테스트 14 〉	통과 (232.49ms, 10.5MB)
테스트 15 〉	통과 (2396.79ms, 10.6MB)
테스트 16 〉	통과 (253.65ms, 10.3MB)
테스트 17 〉	통과 (2103.15ms, 10.5MB)
테스트 18 〉	통과 (1299.96ms, 10.5MB)
테스트 19 〉	통과 (1394.01ms, 10.6MB)
테스트 20 〉	통과 (1307.02ms, 10.3MB)
테스트 21 〉	통과 (1442.29ms, 10.6MB)
테스트 22 〉	통과 (1004.78ms, 10.4MB)
테스트 23 〉	통과 (1442.84ms, 10.6MB)
'''

