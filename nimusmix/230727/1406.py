import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = []
command_cnt = int(input())

for _ in range(command_cnt):
    command = input().split()
    
    if command[0] == 'L':
        if word1:
            word2.append(word1.pop())
    elif command[0] == 'D':
        if word2:
            word1.append(word2.pop())
    elif command[0] == 'B':
        if word1:
            word1.pop()
    else:
        word1.append(command[1])

print(''.join(word1), end='')
print(''.join(list(reversed(word2))))