# 틀린 코드임!!!!
A, B, C = map(int, input().split())

ans = {}

if A <= C and B <= C:
    if A >= B:
        print(1)
        ans = {C, C-B, B, C-A+(C-A-B) if C-A-B>=0 else A}
    else:
        print(2)
        ans = {A, B, C-A, C-B, C}
elif A <= C and B > C:
    print(3)
    ans = {A, C-A, 0, C}
elif A > C and B <= C:
    if A >= B:
        print(4)
        ans = {C, C-B, B}
    else:
        print(5)
        ans = {B, C-B, 0, C}
else:
    print(6)
    ans = {0, C}

print(*sorted(ans))
