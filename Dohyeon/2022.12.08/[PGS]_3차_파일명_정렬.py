def solution(files):
    head_dict = {}
    answer = []
    for i in range(len(files)):
        head_name = ""
        number_name = ""
        number_start = 0
        tail_start = 0
        for j in range(len(files[i])):
            if files[i][j].isnumeric():
                number_start = j
                break
            head_name = head_name + files[i][j]

        for j in range(number_start, len(files[i])):
            if not files[i][j].isnumeric():
                tail_start = j
                break
            number_name = number_name + files[i][j]


        try:
            check = head_dict[head_name.upper()]
            head_dict[head_name.upper()].append([int(number_name), i])

        except KeyError:
            head_dict[head_name.upper()] = [[int(number_name), i]]


    # key list를 뽑아서 키 안의 값들을 numbername 별로 정리하자, 만약 같을 경우 들어온 순서니까 조심
    # 이후 key list를 소팅한 후 소팅된 키리스 안의 값들을 하나씩 집어넣으면 됨
    name_key_list = list(head_dict.keys())
    name_key_list.sort()
    for i in range(len(name_key_list)):
        head_dict[name_key_list[i]].sort(key=lambda x:x[0])
        for j in range(len(head_dict[name_key_list[i]])):
            answer.append(files[head_dict[name_key_list[i]][j][1]])


    return answer


result = solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
print(result)

"""
테스트 1 〉	통과 (0.06ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (2.74ms, 10.5MB)
테스트 4 〉	통과 (2.84ms, 10.6MB)
테스트 5 〉	통과 (2.66ms, 10.6MB)
테스트 6 〉	통과 (2.75ms, 10.6MB)
테스트 7 〉	통과 (5.28ms, 10.3MB)
테스트 8 〉	통과 (4.82ms, 10.5MB)
테스트 9 〉	통과 (2.56ms, 10.4MB)
테스트 10 〉	통과 (2.46ms, 10.5MB)
테스트 11 〉	통과 (2.50ms, 10.5MB)
테스트 12 〉	통과 (2.61ms, 10.5MB)
테스트 13 〉	통과 (2.55ms, 10.6MB)
테스트 14 〉	통과 (3.04ms, 10.7MB)
테스트 15 〉	통과 (3.06ms, 10.6MB)
테스트 16 〉	통과 (2.44ms, 10.6MB)
테스트 17 〉	통과 (2.36ms, 10.4MB)
테스트 18 〉	통과 (2.38ms, 10.5MB)
테스트 19 〉	통과 (2.75ms, 10.4MB)
테스트 20 〉	통과 (2.61ms, 10.4MB)
"""