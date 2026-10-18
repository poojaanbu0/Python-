def non_repeat(str):
    dict = {}

    for char in str:
        dict[char] = dict.get(char, 0) + 1
    
    
    for char in str:
        if dict[char] == 1:
            return char

    return -1

str = input("enter name ")
print(non_repeat(str))