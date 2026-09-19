n = int(input())
num = 1
for i in range(1,n):
    for _ in range(i):
        print(num,end= " ")
        num += 1
    print()