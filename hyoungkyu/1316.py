N = int(input())
count = 0
for i in range(N):
    a = input()
    s = set()
    l = [a[0]]
    for j in a:
        if j == l[-1]:
            pass
        else:
            if j not in l:
                l.append(j)
            else:
                break
    else:
        count += 1
print(count)