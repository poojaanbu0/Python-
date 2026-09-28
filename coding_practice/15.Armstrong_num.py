def armstrong(n):
    count = 0
    num = n
    y = n
    res = 0
    if n == 0:
        count = 1
    while (n != 0):
        count += 1
        n = n // 10

    while(num != 0):
        last_dig = num % 10
        res = res + pow(last_dig , count)
        num = num // 10

    x= "armstrong" if (y == res) else "not armstrong"
    print(x)

n = int(input("enter number "))
armstrong(n)