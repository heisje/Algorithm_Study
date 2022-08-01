#2605 줄세우기
#76ms

#핵심: 본인 num 와 티켓차이가 본인 index이다.
N = int(input())

ticket_li = list(map(int, input().split()))

result = []
for i, ticket in enumerate(ticket_li):
    result.insert(i - ticket, i + 1)
print(*result)
