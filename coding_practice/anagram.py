# def anagram(str1,str2):
#     freq = {}

#     for char in str1:
#         freq[char] = freq.get(char, 0) + 1
#     print(freq)

#     for char1 in str2:
#         if char1 in freq:
#             freq[char1] -= 1

#     print(freq)

#     if all(count==0 for count in freq.values()):
#         print("anagram")
#     else:
#         print("not anagram")
# s = input("str1")
# x = input("str2")
# anagram(s,x)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")

else:
    frequency = {}

    # Increment using first string
    for char in s1:
        frequency[char] = frequency.get(char, 0) + 1

    # Decrement using second string
    for char in s2:
        frequency[char] = frequency.get(char, 0) - 1

    # Check whether all frequencies are 0
    if all(count == 0 for count in frequency.values()):
        print("Anagram")
    else:
        print("Not Anagram")