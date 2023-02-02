# def solution(gems):
#     target = len(set(gems))
#     least = len(gems) + 1
#     for i in range(len(gems) - target):                # 최소 한도의 길이 조건
#
#         for j in range(i + target, len(gems) + 1):     #
#             if j - i >= least:
#                 break
#
#             if len(set(gems[i:j])) == target:
#
#                 answer = []
#                 answer.append(i + 1)
#                 answer.append(j)
#                 least = j - i
#
#     return answer
#
# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

from collections import deque
# ->실패




def solution(gems):
    target = len(set(gems))
    total_len = len(gems)
    start = 0
    end = 0
    gem_kind_dict = {gems[0] : 1}
    answer = [0, 0]
    shortest = len(gems)
    while(start <= end):
        if len(gem_kind_dict) == target:

            if end - start < shortest:
                answer[0] = start + 1
                answer[1] = end + 1
                shortest = end - start
        # print("---------")
        # print(start, end)
        # print(gem_kind_dict)
        # print(len(gem_kind_dict))

        if len(gem_kind_dict) < target:
            end += 1
            if end >= len(gems):
                break

            try:
                gem_kind_dict[gems[end]] += 1

            except KeyError:
                gem_kind_dict[gems[end]] = 1

        else:



            try:
                if gem_kind_dict[gems[start]] > 1:
                    gem_kind_dict[gems[start]] -= 1
                else:
                    gem_kind_dict.pop(gems[start])
                start += 1
            except KeyError:
                print("키에러 발생, 사실상 와서는 안되는 곳")




    return answer

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print("------")
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))

print(solution(["AA", "AB", "AC", "AA", "AC"]))


"""
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (0.30ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.67ms, 10.4MB)
테스트 9 〉	통과 (0.61ms, 10.2MB)
테스트 10 〉	통과 (0.79ms, 10.4MB)
테스트 11 〉	통과 (1.20ms, 10.3MB)
테스트 12 〉	통과 (1.01ms, 10.3MB)
테스트 13 〉	통과 (1.92ms, 10.3MB)
테스트 14 〉	통과 (2.27ms, 10.4MB)
테스트 15 〉	통과 (3.19ms, 10.6MB)
효율성  테스트
테스트 1 〉	통과 (3.40ms, 10.4MB)
테스트 2 〉	통과 (5.66ms, 10.6MB)
테스트 3 〉	통과 (10.47ms, 11.1MB)
테스트 4 〉	통과 (10.48ms, 11.9MB)
테스트 5 〉	통과 (18.06ms, 11.9MB)
테스트 6 〉	통과 (21.67ms, 12.1MB)
테스트 7 〉	통과 (26.37ms, 12.7MB)
테스트 8 〉	통과 (29.29ms, 12.9MB)
테스트 9 〉	통과 (31.76ms, 13.4MB)
테스트 10 〉	통과 (37.32ms, 13.7MB)
테스트 11 〉	통과 (44.14ms, 14.4MB)
테스트 12 〉	통과 (29.75ms, 15.4MB)
테스트 13 〉	통과 (44.48ms, 16.1MB)
테스트 14 〉	통과 (67.76ms, 17MB)
테스트 15 〉	통과 (69.92ms, 17.9MB)
"""