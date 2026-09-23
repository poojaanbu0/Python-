# def prime(n):
#     if n <= 1:
#         return "not a prime number"
#     for i in range(2, n):
#         if n % i == 0:
#             return "not a prime numbmer"
#     return "is prime"

# n=int(input("enter the number "))
# print(prime(n))

def isPrime(n):

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


n=int(input("enter the number "))
print(isPrime(n))