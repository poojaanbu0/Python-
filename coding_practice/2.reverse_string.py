def reverse_string(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    print(reversed_str)

str = input("enter string")
reverse_string(str)