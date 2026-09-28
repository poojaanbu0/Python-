def count_vowels_consonants(string):
    vowels = 0
    consonants = 0

    string = string.lower()

    for char in string:

        if char.isalpha():

            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


string = input("Enter string: ")
count_vowels_consonants(string)