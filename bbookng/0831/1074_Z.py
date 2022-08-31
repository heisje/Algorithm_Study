N, r, c = map(int, input().split())

result = 0
while N > 0:
    N -= 1
    if r // (2 ** N):
        result += (2 ** N) ** 2 * 2

    if c // (2 ** N):
        result += (2 ** N) ** 2

    r = r % (2 ** N)
    c = c % (2 ** N)

print(result)