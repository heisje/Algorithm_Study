"""
def solution(info, query):
    answer = []
    people = []
    for i in range(len(info)):
        people.append(list(info[i].split(" ")))

    for i in range(len(query)):
        tmp = list(query[i].split(" "))
        language = tmp[0]
        type = tmp[2]
        career = tmp[4]
        food = tmp[6]
        score = tmp[7]

        wanted = 0

        for j in range(len(people)):


            if language == '-' or language == people[j][0]:
                if type == '-' or type == people[j][1]:
                    if career == '-' or career == people[j][2]:
                        if food == '-' or food == people[j][3]:
                            if score == '-' or int(score) <= int(people[j][4]):
                                wanted += 1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

        answer.append(wanted)
    return answer


테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.3MB)
테스트 3 〉	통과 (0.78ms, 10.4MB)
테스트 4 〉	통과 (5.34ms, 10.3MB)
테스트 5 〉	통과 (34.33ms, 10.4MB)
테스트 6 〉	통과 (86.28ms, 10.4MB)
테스트 7 〉	통과 (31.74ms, 10.4MB)
테스트 8 〉	통과 (124.37ms, 12.6MB)
테스트 9 〉	통과 (141.19ms, 12.6MB)
테스트 10 〉	통과 (90.12ms, 12.5MB)
테스트 11 〉	통과 (16.92ms, 10.5MB)
테스트 12 〉	통과 (63.35ms, 10.5MB)
테스트 13 〉	통과 (30.42ms, 10.5MB)
테스트 14 〉	통과 (135.07ms, 11.5MB)
테스트 15 〉	통과 (124.58ms, 11.4MB)
테스트 16 〉	통과 (26.32ms, 10.4MB)
테스트 17 〉	통과 (55.55ms, 10.3MB)
테스트 18 〉	통과 (126.56ms, 11.5MB)
"""
from collections import deque
"""
def solution(info, query):
    answer = []
    people = {'language':{'java':[], 'cpp':[], 'python':[]}, 'type':{'backend':[], 'frontend':[]},
              'career':{'junior':[], 'senior':[]}, 'food':{'chicken':[],'pizza':[]}, 'score': []}

    for i in range(len(info)):
        people_list = list(info[i].split(" "))

        people['language'][people_list[0]].append(i)
        people['type'][people_list[1]].append(i)
        people['career'][people_list[2]].append(i)
        people['food'][people_list[3]].append(i)
        people['score'].append((people_list[4], i))


    for i in range(len(query)):


        query_list = list(query[i].split(" "))
        if query_list[0] == 'java':
            language_set = set(people['language']['java'])
        elif query_list[0] == 'cpp':
            language_set = set(people['language']['cpp'])
        elif query_list[0] == 'python':
            language_set = set(people['language']['python'])
        else:
            language_set = set(people['language']['python']) | set(people['language']['cpp']) | set(people['language']['java'])

        if query_list[2] == 'backend':
            type_set = set(people['type']['backend'])
        elif query_list[2] == 'frontend':
            type_set = set(people['type']['frontend'])
        else:
            type_set = set(people['type']['backend']) | set(people['type']['frontend'])

        if query_list[4] == 'junior':
            career_set = set(people['career']['junior'])
        elif query_list[4] == 'senior':
            career_set = set(people['career']['senior'])
        else:
            career_set = set(people['career']['junior']) | set(people['career']['senior'])

        if query_list[6] == 'pizza':
            food_set = set(people['food']['pizza'])
        elif query_list[6] == 'chicken':
            food_set = set(people['food']['chicken'])
        else:
            food_set = set(people['food']['pizza']) | set(people['food']['chicken'])

        score_set = []
        if query_list[7] == '-':
            for j in range(len(people['score'])):
                score_set.append(people['score'][j][1])
        else:
            for j in range(len(people['score'])):
                if int(people['score'][j][0]) >= int(query_list[7]):
                    score_set.append(people['score'][j][1])

        score_set = set(score_set)
     
        print("-----------")
        print(query_list)
        print(language_set)
        print(type_set)
        print(career_set)
        print(food_set)
        print(score_set)
  

        answer.append(len(language_set & type_set & career_set & food_set & score_set))
    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))


테스트 1 〉	통과 (0.26ms, 10.5MB)
테스트 2 〉	통과 (0.16ms, 10.4MB)
테스트 3 〉	통과 (1.89ms, 10.5MB)
테스트 4 〉	통과 (11.41ms, 10.4MB)
테스트 5 〉	통과 (55.40ms, 10.5MB)
테스트 6 〉	통과 (123.65ms, 10.7MB)
테스트 7 〉	통과 (69.76ms, 10.7MB)
테스트 8 〉	통과 (255.36ms, 14MB)
테스트 9 〉	통과 (290.89ms, 14.5MB)
테스트 10 〉	통과 (322.60ms, 14.3MB)
테스트 11 〉	통과 (48.26ms, 10.5MB)
테스트 12 〉	통과 (117.00ms, 10.6MB)
테스트 13 〉	통과 (55.45ms, 10.7MB)
테스트 14 〉	통과 (285.84ms, 12.1MB)
테스트 15 〉	통과 (318.06ms, 12.1MB)
테스트 16 〉	통과 (53.57ms, 10.6MB)
테스트 17 〉	통과 (127.36ms, 10.7MB)
테스트 18 〉	통과 (251.02ms, 12MB)
"""

# 정답코드

from itertools import combinations


def solution(info, query):
    answer = []
    db = {}
    for i in info:  # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]  # 조건들만 모으고, 점수 따로
        score = int(temp[-1])
        for n in range(5):  # 조건들에 대해 조합을 이용해서
            combi = list(combinations(range(4), n))
            print(combi)
            for c in combi:
                t_c = conditions.copy()
                for v in c:  # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:  # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():  # 딕셔너리 내 모든 값 정렬
        value.sort()

    for q in query:  # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))

"""
값이 클수록 속도차이가 심해짐
테스트 1 〉	통과 (0.29ms, 10.4MB)
테스트 2 〉	통과 (0.28ms, 10.3MB)
테스트 3 〉	통과 (0.67ms, 10.5MB)
테스트 4 〉	통과 (2.27ms, 10.3MB)
테스트 5 〉	통과 (3.05ms, 10.4MB)
테스트 6 〉	통과 (11.00ms, 10.4MB)
테스트 7 〉	통과 (4.58ms, 10.7MB)
테스트 8 〉	통과 (58.04ms, 11.2MB)
테스트 9 〉	통과 (55.41ms, 11.2MB)
테스트 10 〉	통과 (56.00ms, 11.4MB)
테스트 11 〉	통과 (3.21ms, 10.6MB)
테스트 12 〉	통과 (6.40ms, 10.4MB)
테스트 13 〉	통과 (4.01ms, 10.7MB)
테스트 14 〉	통과 (27.72ms, 10.8MB)
테스트 15 〉	통과 (43.33ms, 11MB)
테스트 16 〉	통과 (3.03ms, 10.3MB)
테스트 17 〉	통과 (6.54ms, 10.4MB)
테스트 18 〉	통과 (27.73ms, 10.9MB)
효율성  테스트
테스트 1 〉	통과 (1045.45ms, 39.5MB)
테스트 2 〉	통과 (1051.60ms, 39.3MB)
테스트 3 〉	통과 (1110.78ms, 39.5MB)
테스트 4 〉	통과 (1116.81ms, 39MB)
"""