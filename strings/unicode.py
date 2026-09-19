n = "AalaminfoSolutionsccp"
x = n.lower()
print(x)
count = 0
# x = [ord(char) for char in n]
# print(x)

# def count_letters_with_ord(text):
    
#     counts = [0] * 26  
    
  
#     for char in n.lower():  
#         if 'a' <= char <= 'z':
#             # checking if its a character
#             index = ord(char) - ord('a')   # int value of a is standard and other values are away from it.
#             counts[index] += 1
            
    
#     for i in range(26):
#         if counts[i] > 0:
#             print(f"{chr(i + ord('a'))}: {counts[i]}")


# count_letters_with_ord("AalaminfoSolutionsccp")


# count = {}
# for char in x:
#     if char.isalpha:
#         count[char]=  count.get(char,0) +1
# print(count)

from collections import Counter

counts = Counter(char for char in x if char.isalpha())
print(counts)


