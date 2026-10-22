# def prime(n):
#     if n <= 1:
#         return "not a prime number"
#     for i in range(2, n):
#         if n % i == 0:
#             return "not a prime numbmer"
#     return "is prime"

# n=int(input("enter the number "))
# print(prime(n))

def prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def sum(num):
    total = 0

    for n in range(2,num+1):
        if prime(n):
            total += n

    return total

n=int(input("enter the number "))
print(sum(n))