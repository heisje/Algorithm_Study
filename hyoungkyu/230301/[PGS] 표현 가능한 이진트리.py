def get_length(num):
    n = 0
    while True:
        n += 1
        if 2**(2**n-1) > num:
            return 2**n-1
        
def sub_tree(tree, tot):
    root = int(tree[len(tree)//2])
    if len(tree) > 1 and root == 0 and tree.count('1'):
        tot += 1
    elif len(tree) > 1:
        tot += sub_tree(tree[0:len(tree)//2], tot)
        tot += sub_tree(tree[len(tree)//2+1:], tot)
    return tot

def solution(numbers):
    answer = []
    
    for num in numbers:
        length = get_length(num)
        binary_num = bin(num).lstrip('0').lstrip('b')
        binary_num = '0'*(length-len(binary_num)) + binary_num
        
        check = sub_tree(binary_num, 0)
        # print(binary_num, check)
        answer.append(0 if check else 1)
    return answer

'''
1 3 7 15 31 ...
2 8 128

1  -  1

2  -  010
3  -  011
4  -  100 X
5  -  101 X
6  -  110
7  -  111

8  -  0001000
9  -  0001001 X
10 -  0001010
11 -  0001011
12 -  0001100 X
13 -  0001101 X
14 -  0001110
15 -  0001111
16 -  0010000 X
17 -  0010001 X
18 -  0010010 X
19 -  0010011 X
20 -  0010100 X
'''

'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.28ms, 10.3MB)
테스트 5 〉	통과 (0.91ms, 10.4MB)
테스트 6 〉	통과 (1.01ms, 10.5MB)
테스트 7 〉	통과 (2.27ms, 10.4MB)
테스트 8 〉	통과 (0.89ms, 10.4MB)
테스트 9 〉	통과 (7.74ms, 10.5MB)
테스트 10 〉	통과 (69.79ms, 11.2MB)
테스트 11 〉	통과 (74.83ms, 11.4MB)
테스트 12 〉	통과 (70.16ms, 11.3MB)
테스트 13 〉	통과 (62.55ms, 11.2MB)
테스트 14 〉	통과 (69.54ms, 11.3MB)
테스트 15 〉	통과 (65.23ms, 10.9MB)
테스트 16 〉	통과 (131.85ms, 11.5MB)
    테스트 17 〉	통과 (141.69ms, 11.5MB)
테스트 18 〉	통과 (114.58ms, 11.2MB)
테스트 19 〉	통과 (102.62ms, 11.2MB)
테스트 20 〉	통과 (67.16ms, 10.8MB)
'''