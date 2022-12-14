# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 20분
def solution(progresses, speeds):
    answer = []
    succeed_li = [0 for _ in range(len(progresses))]
    succeed_count = 0
    len_all = len(progresses)
    while succeed_count < len_all:
        # print(progresses)
        # print(succeed_li)
        # print(succeed_count)
        # 점수를 누적해!
        for idx, _ in enumerate(progresses):

            # 점수를 누적해!
            if succeed_li[idx] == 0:
                progresses[idx] += speeds[idx]

                # 점수 초과되면 1로 바꿔!
                if progresses[idx] >= 100:
                    succeed_li[idx] = 1

        # 성공하면 2로 바꾼다.
        for idx, value in enumerate(succeed_li):
            if value == 1 and (idx == 0 or succeed_li[idx-1] == 2 or succeed_li[idx-1] == 3):
                succeed_li[idx] = 2
                

        # 결과 계산
        count = succeed_li.count(2)
        if count > 0:
            # 계산된 게 있으면 결과값 누적
            succeed_count += count
            answer.append(count)
            # 결과를 계산하고 2->3으로 바꿔서 개수셀때 오류안나게한다..
            for idx in range(len(succeed_li)):
                if succeed_li[idx] == 2:
                    succeed_li[idx] = 3

    return answer

a = [93, 30, 55]
b = [1, 30, 5]
print(solution(a,b))
a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]
print(solution(a,b))


# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (1.09ms, 10.2MB)
# 테스트 3 〉	통과 (1.18ms, 10.2MB)
# 테스트 4 〉	통과 (0.68ms, 10.2MB)
# 테스트 5 〉	통과 (0.05ms, 10.2MB)
# 테스트 6 〉	통과 (0.15ms, 10.2MB)
# 테스트 7 〉	통과 (1.50ms, 10.3MB)
# 테스트 8 〉	통과 (0.17ms, 10.3MB)
# 테스트 9 〉	통과 (0.94ms, 10.3MB)
# 테스트 10 〉	통과 (0.82ms, 10.4MB)
# 테스트 11 〉	통과 (0.02ms, 10.2MB)