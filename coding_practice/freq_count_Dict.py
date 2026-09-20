# def frequency(a):
#     freq = {}

#     for num in a:
#         freq[num] = freq.get(num,0) + 1
#     print(freq)

# s = list(map(int, input("enter array").split()))
# frequency(s)

# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(list(res))
# print(list(res))

def palindrome(str):
    x = ""
    for char in str:
        x = char + x

    if (x==str):
        print("palindrome")
    else:
        print("not palindrome")

str = input("Enter str")

palindrome(str)