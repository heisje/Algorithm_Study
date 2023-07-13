# 실버2
def cal(eq):
    res = 0
    tmp = ''
    for i in eq:
        if i == "+":
            res += int(tmp)
            tmp = ''
        else:
            tmp += i
    if tmp:
        res += int(tmp)
    return res

eq = input()

parse = eq.split('-')

ans = cal(parse.pop(0))

for i in parse:
    ans -= cal(i)

print(ans)
