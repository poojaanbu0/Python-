# def reverse_string(str):
#     reversed_str = ""
#     for char in str:
#         reversed_str = char + reversed_str
#     print(reversed_str)

# str = input("enter string")
# reverse_string(str)

def reverse(sentec):
    words = sentec.split()
    result = []

    for i in range(len(words) - 1, -1, -1):
        result.append(words[i])

    return " ".join(result)
sentec = input("enter string ")
print(reverse(sentec))