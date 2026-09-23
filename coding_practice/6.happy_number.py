# happy number = sum of its square of its digits
# 19 = sq(1) + sq(9) = 1 + 81 = 82 => sq(2) + sq(8) = 4 + 64 = 68 => 36 + 64 = > 100 => 1 + 0 + 0 = 1
import math
def happy_number(n):
    
    while sq != 1:
        x = n % 10
        sq_x = math.pow(x, 2)
        y = n // 10
        sq_y = math.pow(y, 2)
        sq=int(sq_x) + int(sq_y)
        print(sq)
    

n = int(input("enter a num "))
happy_number(n)