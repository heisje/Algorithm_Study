import sys
input = sys.stdin.readline

switch = int(input())
status = list(map(int, input().split()))
students = int(input())

def onoff(x):                                   # 스위치의 상태를 변경할 함수
    if status[x] == 0: status[x] = 1
    else: status[x] = 0
    
def list_chunk(li):                             # 리스트를 20개씩 나눌 함수
    return [li[i:i+20] for i in range(0, switch, 20)]

for _ in range(students):
    s, n = map(int, input().split())
    c_li = []
    
    if s == 1:                                  # 남자이면
        for i in range(n, switch+1, n):
            onoff(i-1)
    else:                                       # 여자이면
        n -= 1
        onoff(n)
        
        for i in range(1, switch//2):
            if n+i > switch-1 or n-i < 0: break
            if status[n-i] == status[n+i]:
                onoff(n-i)
                onoff(n+i)
            else: break

status = list_chunk(status)
for i in status:
    print(*i)