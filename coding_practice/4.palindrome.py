def palindrome(str):
    x = ""
    for char in str:
        x = char + x

    if (x==str):
        print("palindrome")
    else:
        print("not palindrome")

str = input("Enter str").replace(" ","")
print(str)
palindrome(str)