max_gap = -56
answers = []
count = 0
max_depth = 0
def ShootOrNot(info, history, index, arrow):

    global max_gap
    global answers
    global count
    global max_depth

    if arrow == 0:
        if len(history) < 11:
            for i in range(11 - len(history)):
                history.append(0)
        sum_of_history_ap = 0
        sum_of_history_li = 0
        for i in range(11):
            if history[i]:
                sum_of_history_li += 10 - i
            else:
                if info[i]:
                    sum_of_history_ap += 10 - i
        gap = sum_of_history_li - sum_of_history_ap
        if gap >= max_gap:
            if gap > max_gap:
                answers.clear()
                max_depth = 0
                count = 1
            else:
                count += 1

            if max_depth <= index:
                answers.append(history)
                max_depth = index
            else:
                answers.insert(0, history)

            max_gap = gap

        return

    if index == 11:


        sum_of_history_ap = 0
        sum_of_history_li = 0
        if arrow:
            history[-1] = history[-1] + arrow

        for i in range(11):
            if history[i]:
                sum_of_history_li += 10 - i
            else:
                if info[i]:
                    sum_of_history_ap += 10 - i
        gap = sum_of_history_li - sum_of_history_ap
        if gap >= max_gap:
            if gap > max_gap:
                answers.clear()
                max_depth = 0
                count = 0
            else:
                count += 1
            if max_depth <= index:
                answers.append(history)
                max_depth = index
            else:
                answers.insert(0, history)

            max_gap = gap
        return


    if info[index] >= arrow:    # 여기 다 쏴봤자 안됨
        ShootOrNot(info, history + [0], index + 1, arrow)
    else:
        ShootOrNot(info, history + [0], index + 1, arrow)
        ShootOrNot(info, history + [info[index] + 1], index + 1, arrow - (info[index] + 1))



def solution(n, info):
    global max_gap
    global answers
    global count
    ShootOrNot(info, [], 0, n)

    if max_gap <= 0:
        answer = [-1]
    else:
        answer = answers[-1]

    return answer

"""
테스트 1 〉	통과 (0.11ms, 10.5MB)
테스트 2 〉	통과 (1.87ms, 10.3MB)
테스트 3 〉	통과 (1.59ms, 10.3MB)
테스트 4 〉	통과 (1.19ms, 10.3MB)
테스트 5 〉	통과 (2.87ms, 10.3MB)
테스트 6 〉	통과 (1.76ms, 10.3MB)
테스트 7 〉	통과 (1.14ms, 10.3MB)
테스트 8 〉	통과 (0.25ms, 10.4MB)
테스트 9 〉	통과 (1.21ms, 10.4MB)
테스트 10 〉	통과 (0.23ms, 10.2MB)
테스트 11 〉	통과 (0.78ms, 10.3MB)
테스트 12 〉	통과 (0.77ms, 10.2MB)
테스트 13 〉	통과 (1.41ms, 10.3MB)
테스트 14 〉	통과 (1.85ms, 10.2MB)
테스트 15 〉	통과 (3.03ms, 10.2MB)
테스트 16 〉	통과 (0.88ms, 10.2MB)
테스트 17 〉	통과 (0.78ms, 10.3MB)
테스트 18 〉	통과 (0.13ms, 10.3MB)
테스트 19 〉	통과 (0.05ms, 10.3MB)
테스트 20 〉	통과 (2.91ms, 10.3MB)
테스트 21 〉	통과 (1.57ms, 10.2MB)
테스트 22 〉	통과 (3.50ms, 10.2MB)
테스트 23 〉	통과 (0.44ms, 10.2MB)
테스트 24 〉	통과 (2.45ms, 10.3MB)
테스트 25 〉	통과 (1.76ms, 10.3MB)
"""