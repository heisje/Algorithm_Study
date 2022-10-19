"""
"{{2},{2,1},{2,1,3},{2,1,3,4}}"
"{{1,2,3},{2,1},{1,2,4,3},{2}}"
"{{20,111},{111}}"
"{{123}}"
"{{4,2,3},{3},{2,3,4,1},{2,3}}"
"""

def solution(s):

    answer = []
    list_dict = {}
    total = 0
    cnt = 0
    start = False
    temp = []
    temp_num = ""
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] == "{" and not start:
            start = True
            continue
        if s[i].isdecimal():
            temp_num = temp_num + s[i]
            continue
        if s[i] == "," and start:
            temp.append(int(temp_num))
            temp_num = ""
            cnt += 1
            continue

        if s[i] == "}" and start:
            temp.append(int(temp_num))
            temp_num = ""
            cnt += 1
            start = False
            list_dict[cnt] = temp
            temp = []
            total += 1
            cnt = 0
    before_set = {-1}
    for i in range(1, total + 1):
        tmp_set = set(list_dict[i])
        answer.append(*(tmp_set - before_set))
        before_set = tmp_set


    return answer

print(solution("{{20,111},{111}}"))