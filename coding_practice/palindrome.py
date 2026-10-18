# def palindrome(str):
#     x = ""
#     for char in str:
#         x = char + x

#     if (x==str):
#         print("palindrome")
#     else:
#         print("not palindrome")

# str = input("Enter str").replace(" ","")
# print(str)
# palindrome(str)


#using recursion

def palindrome(str, left , right):

    if left >= right:
        return True

    if str[left] != str[right]:
        return False

    return palindrome(str, left + 1, right - 1)
    
str = input("enter the value ")
print(palindrome(str, 0 , len(str) - 1))

