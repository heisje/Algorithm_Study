from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])

    cols_list = list(range(cols))
    result = []
    for i in range(cols + 1):
        result = result + list(combinations(cols_list, i))   # 사용가능한 col의 조합을 다 모아둔다.


    done = []
    for case in result:
        if len(case) == 0:
            continue
        check = False
        for did in done:
            if set(did).issubset(set(case)):        # 부분집합안에 포함되는 경우 둘째조건 만족 x
                check = True
        if check:
            continue
        temp = ['0']*rows
        for col in case:
            for i in range(rows):
                temp[i] = temp[i] + relation[i][col]

        if len(set(temp)) == rows:                  # 두 열을 합친후 set한 값이 행의 수와 같으면 중복은 없다.
            done.append(case)
        else:
            continue

    answer = len(done)
    return answer