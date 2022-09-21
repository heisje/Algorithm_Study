length = int(input())
len_S = int(input())
S = input()

pattern = "I" + ("OI" * length)
len_P = len(pattern)
total = 0
count = 0                                   # IO 다음 I가 몇번이 오는지 확인해보자
maching_count = length
I_check1 = False
O_check1 = False
I_check2 = False
O_check2 = False

for i in range(len_S):
    if i == 0:
        if S[i] == "O":
            continue
        else:
            I_check1 = True
    else:
        if I_check1:
            if S[i] == "O":
                I_check1 = False
                O_check1 = True
            else:
                continue

        elif O_check1:
            if S[i] == "O":
                O_check1 = False
            else:
                I_check2 = True
                O_check1 = False
                count = 1

        elif I_check2:
            if S[i] == "O":
                O_check2 = True
                I_check2 = False
            else:
                if count >= maching_count:
                    total = total + count - maching_count + 1
                count = 0
                I_check2 = False
                I_check1 = True

        elif O_check2:
            if S[i] == "O":
                if count >= maching_count:
                    total = total + count - maching_count + 1
                count = 0
                O_check2 = False
            else:
                I_check2 = True
                O_check2 = False
                count += 1

        else:
            if S[i] == "O":
                continue
            else:
                I_check1 = True
else:
    if count >= maching_count:
        total = total + count - maching_count + 1

print(total)



