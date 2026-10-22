def decimal_binary(b):

    if b == 0:
        return "0"
    
    binary = ""
    while b > 0:
        remainder = b % 2
        binary = str(remainder) + binary
        b = b // 2 
    return binary

    # result = 0

    # for dig in b:
    #     result = result * 2 + int(dig)

    # return result 

b = int(input("enter the num "))
print(decimal_binary(b))