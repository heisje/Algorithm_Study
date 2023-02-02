def solution(gems):
    left, right = 0, 0
    gems_cnt = len(set(gems))

    gems_dict = dict()

    while right < len(gems) + 1:
        if gems[right] in gems_dict:
            gems_dict[gems[right]] += 1
        else:
            gems_dict[gems[right]] = 1

        right += 1

        if len(gems_dict) == gems_cnt:
            while left < right:
                if gems_dict[gems[left]] > 1:
                    gems_dict[gems[left]] -= 1
                    left += 1
                else:
                    return [left + 1, right]



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
