def fact(n):
    if n == 1 or n == 0 :
        return 1

    return n * fact(n - 1)

def strong(n):
    temp = n
    sum = 0
    while(n != 0):
        digit = n % 10 
        sum += fact(digit)
        n //= 10
    return temp == sum



n = int(input("enter num "))
if (strong(n)):
    print("strong")
else:
    print("no strong")