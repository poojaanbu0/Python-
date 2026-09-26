def gcd(a,b):
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    print(a)

a = int(input("enter no1 "))
b = int(input("enter no2 "))
gcd(a,b)