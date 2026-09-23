# # happy number = sum of its square of its digits
# # 19 = sq(1) + sq(9) = 1 + 81 = 82 => sq(2) + sq(8) = 4 + 64 = 68 => 36 + 64 = > 100 => 1 + 0 + 0 = 1

def happy_number(num):

    seen = set()

    while num != 1:

        # Check whether this number was already encountered
        if num in seen:
            return "Not a Happy Number"

        # Store current number
        seen.add(num)

        # Find sum of squares of digits
        square_sum = 0

        while num > 0:
            digit = num % 10
            square_sum = square_sum + (digit * digit)
            num = num // 10

        # Use the square sum as the next number
        num = square_sum

    return "Happy Number"


num = int(input("Enter number: "))

print(happy_number(num))
