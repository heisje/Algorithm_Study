n = int(input())
draw = input().split()

queue = [1]
idx = 0
for d in draw[1:]:
    idx += 1
    queue.insert(int(idx) - int(d), int(idx) + 1)

for q in queue:
    print(q, end=' ')

'''이렇게 수정하니까 8ms가 늘어났다.
n = int(input())
draw = input().split()

queue = [1]
idx = 1
for d in draw[1:]:
    queue.insert(idx - int(d), idx + 1)
    idx += 1

for q in queue:
    print(q, end=' ')
'''

'''한 사람이 뽑은 자리로 가기 전에 제일 뒤에 서서 대기한다고 하면,
'대기하는 자리의 인덱스'는 '그 사람의 번호 - 1'이다.
새로 들어가는 자리는 (대기하는 자리의 인덱스 - 뽑은 숫자)와 같고,
List.insert() 메서드를 이용하면 쉽게 구현할 수 있었다.

insert() 메서드가 없다면 어떻게 구현 가능할지 궁금하다.

mini_log
1. 처음에 draw.index(d)를 사용하려고 했는데 해당 항목의 제일 첫 번째 위치만 반환하는 거라서 계속 답이 안 나왔다.
2. 출력 형식 안 맞춰서 틀렸었다.
'''
