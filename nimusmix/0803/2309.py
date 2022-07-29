hobbit = []

for i in range(9):
    h = int(input())
    hobbit.append(h)

for j in hobbit:
    for k in hobbit:
            if j != k:
                if sum(hobbit) - j - k == 100:
                    hobbit.remove(j)
                    hobbit.remove(k)

hobbit.sort()
print(*hobbit, sep='\n')