import math
n = 7
i = 1
while i<n:
    if n % i == 0:
        print("not prime")
        break
    i += 1
    print("prime")


num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number:", reverse)

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

total = 0
count = 0

largest = None
smallest = None

even = 0
odd = 0

while True:

    num = int(input("Enter Number (-1 to stop): "))

    if num == -1:
        break

    total += num
    count += 1

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if count > 0:

    print("Sum =", total)
    print("Average =", total / count)
    print("Largest =", largest)
    print("Smallest =", smallest)
    print("Even Count =", even)
    print("Odd Count =", odd)

else:
    print("No Numbers Entered")