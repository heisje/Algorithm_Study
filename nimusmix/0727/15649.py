from itertools import permutations

a, b = map(int, input().split())

for i in permutations(range(1,a+1), b):
    print(*i)