import sys

C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
seats = [[] for _ in range(R)]

for j in range(R, 0, -1):
    for i in range(1, C + 1):
        seats[R - j].append((i, j))
print(seats)

n = 0
seat = [1, 1]
r = R
c = C

if R >= C:
    while r >= R - (C - 1):
        for dir in ['u', 'r', 'd', 'l']:
            if dir == 'u':
                for _ in range(r - 1):
                    n += 1
                    seat[1] += 1
                    if n == K:
                        print(*seat)
                        break
                else:
                    r -= 1
            elif dir == 'r':
                for _ in range(c - 1):
                    n += 1
                    seat[0] += 1
                    if n == K:
                        print(*seat)
                        break
                else:
                    c -= 1
            elif dir == 'd':
                for _ in range(r):
                    n += 1
                    seat[1] -= 1
                    if n == K:
                        print(*seat)
                        break
                else:
                    r -= 1
            else:
                for _ in range(c - 1):
                    n += 1
                    seat[0] -= 1
                    if n == K:
                        print(*seat)
                        break
                else:
                    c -= 1
        if n > K:
            print(0)
            break    



        

# else:
#     while n != K and c >= C - R:
#         n += 1
