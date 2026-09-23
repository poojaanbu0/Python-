def fact(num):
    if num == 1 or num == 0 :
        return 1

    return num * fact(num - 1)

num = int(input("ENter num to cal falctorial "))
print(fact(num))

def fibo(num):
    if num == 0 or num < 0:
        return 0
    if num == 1:
        return 1
    x = fibo(num - 1) + fibo(num - 2)
    return x

num = int(input("ENter num to cal falctorial "))
print(fibo(num))