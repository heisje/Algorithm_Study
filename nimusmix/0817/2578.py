my_bingo = [list(map(int, input().split())) for _ in range(5)]
ans_bingo = []
bingo = cnt = 0

for _ in range(5):
    ans_bingo.extend(list(map(int, input().split())))
    
for ans in ans_bingo:
    bingo = 0
    for j in my_bingo:
        if ans in j:
            j[j.index(ans)] = 0
            cnt += 1

    for j in my_bingo:
        if sum(j) == 0:
            bingo += 1

    sumCross1 = sumCross2 = 0        
    for col in range(5):
        sumCol = 0
        sumCross1 += my_bingo[col][col]
        sumCross2 += my_bingo[col][4-col]
        for row in range(5):
            sumCol += my_bingo[row][col]
        if sumCol == 0:
            bingo += 1
            
    if sumCross1 == 0:
        bingo += 1
    if sumCross2 == 0:
        bingo += 1
                
    if bingo >= 3:
        print(cnt)
        break