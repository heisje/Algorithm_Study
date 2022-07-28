n = int(input())
draw = input().split()

queue = [1]
idx = 0
for d in draw[1:]:
    idx += 1
    queue.insert(int(idx) - int(d), int(idx) + 1)

for q in queue:
    print(q, end=' ')

"""다음 사람이 뽑은 자리로 가기 전에 제일 뒤에 서서 대기한다고 하면,
'대기하는 자리의 인덱스'는 '뽑은 숫자의 인덱스'와 같고,
새로 들어가는 자리는 (대기하는 자리의 인덱스 - 뽑은 숫자)와 같은 것을 구현했다.

mini_log
1. 처음에 draw.index(d)를 사용하려고 했는데 해당 항목의 제일 첫 번째 위치만 반환하는 거라서 계속 답이 안 나왔다.
2. 출력 형식 안 맞춰서 틀렸었다.
"""