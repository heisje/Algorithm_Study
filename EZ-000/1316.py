N = int(input())
c = 0
for n in range(N):
    w = input()
    char_list = list(w)
    
    temp = char_list[:]
    for n in range(len(char_list) - 1):
        if char_list[n] == char_list[n + 1]:
            temp[n] = ''
        elif char_list[n] == char_list[n - 1]:
            temp[n] = ''

    for f in range(temp.count('')):
        temp.remove('')
    
    if temp != []:
        c += 1

print(c)