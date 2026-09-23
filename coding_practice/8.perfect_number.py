# def perfect_num(num):
#     Sum_divisor = 0
#     for i in range(1, num):
#         if num % i == 0:
#             Sum_divisor += i
#     print(Sum_divisor)
#     if Sum_divisor == num:
#         print("perfect number")
#     else:
#         print("not a perfect number")

# n = int(input("enter a num "))
# perfect_num(n)

def perfect_num(num):

    if num <= 1:
        return False

    sum_divisor = 1

    i = 2

    while i * i <= num:

        if num % i == 0:

            # First divisor
            sum_divisor += i

            # Paired divisor
            if i != num // i:
                sum_divisor += num // i

        i += 1
    print(sum_divisor)
    return sum_divisor == num


num = int(input("Enter a number: "))

if perfect_num(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")