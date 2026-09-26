def gcd(a,b):
    x = a 
    y = b
    while(y != 0):
        temp = y
        y = x % y
        x = temp
    lcm = (a * b) / x
    print(lcm)

a = int(input("enter no1 "))
b = int(input("enter no2 "))
gcd(a,b)