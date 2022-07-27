import copy

N, M = map(int, input().split())

original_list = list(range(1, N+1)) # 1부터 N까지 들어있는 리스트

NPM = 1
for i in range(M):
    NPM = (N - i) * NPM # 원하는 순열의 갯수 nPm 계산

result = [[] for i in range(NPM)] # result라는 리스트 안에 순열의 수만큼 빈 리스트가 들어있음

# key idea : 재귀의 윗 단계에서 좌표를 정해주면, 호출된 함수에서 그 좌표안에만 집어넣음

def make_line(choice_list, choice_num, start, cases):  # 뽑을 수 있는 수만 남은 리스트, 뽑아야하는 숫자 수, 시작 idx, 경우의 수
    if choice_num == 1: # 하나만 더 뽑으면 되는 경우
        for last in range(len(choice_list)): # 뽑을 수 있는 수 중 하나를 뽑음
            result[start + last].append(choice_list[last]) # 정해준 시작 좌표 부터 한칸 씩 넣을 수 있는 숫자를 넣어줌
        return None

    count = start # 윗단계에서 지정해준 시작좌표
    for i in range(len(choice_list)): # 넣을 수 있는 숫자 종류만큼 반복
        
        input_list = copy.deepcopy(choice_list) # 함수 호출할 때 넣어줄 리스트를 깊은 복사해 둔다
        for_each = int(cases / len(choice_list)) # i번째 숫자가 들어갈 수 있는 칸 수, 현재 주어진 칸수에 넣을 수 있는 숫자 수를 나누면 된다
        for j in range(count, count + for_each): # 특정 구간에는 특정 숫자만 넣음, 시작 지점 + 들어갈 수 있는 칸수
            result[j].append(choice_list[i]) # 특정 좌표에 i번째 수를 집어넣음
        input_list.pop(i) # i번째 수는 집어넣었으니 복사된 리스트에서 빼버림

        make_line(input_list, choice_num - 1, count, int(cases/len(choice_list))) # i번째 수를 뺀 리스트, 하나 뽑았으니 하나 덜 뽑으면 됨, i번째 수가 들어간 시작지점, i번째 수가 들어간 구간 
        count = count + for_each # i번 째 수가 들어간 구간 다음에 i + 1번 째 수를 넣어주기 위해 count에 i번째 수 구간을 더함
        
    return None # result에 값이 저장되고 있으므로 리턴할 것은 없음

make_line(original_list, M, 0, NPM)

for i in result:
    for j in range(len(i)): # 출력값을 깔끔하게 정리하기 위한 부분, 마지막 글자 뒤엔 공백없이 출력함
        if j == (len(i) - 1):
            print(i[j])
        else:
            print(i[j], end=' ')
