N = int(input())

di_idx = []
di_data = []
double = []
max_x = max_y = 0

for i in range(6):
    a, b = map(int, input().split())
    
    if a in di_idx:
        double.append(a)
        
    di_idx.append(a)
    di_data.append(b)
    
    if a == 1 or a == 2:
        if b > max_x:
            max_x = b
    else:
        if b > max_y:
            max_y = b

double = double*2
r_double = list(reversed(double))

for j in double, r_double:
    for i in range(3):
        if di_idx[i:i+4] == j:
            mini = di_data[i+1] * di_data[i+2]
            
    if di_idx[0] == j[0] and di_idx[3:6] == j[1:4]:
        mini = di_data[-1] * di_data[-2]
    elif di_idx[:3] == j[:3] and di_idx[-1] == j[-1]:
        mini = di_data[0] * di_data[1]
    elif di_idx[:2] == j[:2] and di_idx[4:6] == j[2:4]:
        mini = di_data[0] * di_data[-1]
        
print(N * (max_x * max_y - mini))