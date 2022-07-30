n = int(input())
students = []                           # 최종 순서 list
arr = list(map(int, input().split()))   # 뽑은 번호 list


# i-arr[i]은 뽑은 번호만큼 앞으로 가서 줄 서게 되는 위치
# i+1 은 해당 순서 학생
# students list에 i-arr[i] 위치에 i+1 을 위치시켜줌
for i in range(n):
    students.insert(i-arr[i], i+1)

print(*students)