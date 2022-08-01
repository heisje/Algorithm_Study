N = int(input())

ticket_li = list(map(int, input().split()))

result = []
for i, ticket in enumerate(ticket_li):
    result.insert(i - ticket, i + 1)
print(*result)
