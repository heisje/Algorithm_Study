# 실버1 / 40ms
S = input()*2
len_a = S.count('a') // 2

min_v = len_a
for i in range(len(S)-len_a+1):
    min_v = min(S[i:i+len_a].count('b'), min_v)
print(min_v)

'''
8 12
aabbaaabaaba
aabbaaab - 3
 abbaaaba - 3
  bbaaabaa - 3
   baaabaab - 3
    aaabaaba - 2
'''