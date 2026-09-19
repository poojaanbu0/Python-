
student = {
    "name": "Pooja",
    "age": 22,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# ======================================================
# Problem  : Frequency of Characters
# ======================================================

text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# ======================================================
# Problem  : Frequency of Words
# ======================================================


sentence = input("Enter sentence: ").lower()

freq = {}

for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)

# ======================================================
# Problem  : Dictionary Sort by Value
# ======================================================

marks = {
    "Ram":78,
    "John":91,
    "Sam":82,
    "Asha":69
}

sorted_marks = dict(
    sorted(
        marks.items(),
        key=lambda x:x[1]
    )
)

print(sorted_marks)


# ======================================================
# Problem : Inventory System
# ======================================================

inventory = {
    "Laptop":10,
    "Mouse":25,
    "Keyboard":15
}

while True:

    print("\nInventory")

    for item,qty in inventory.items():
        print(item,"-",qty)

    product = input("\nProduct: ").title()

    if product not in inventory:
        print("Item Not Found")

    else:

        buy = int(input("Quantity: "))

        if buy > inventory[product]:
            print("Only",inventory[product],"available")

        else:
            inventory[product]-=buy
            print("Purchased Successfully")

    again=input("Continue(y/n): ")

    if again.lower()=="n":
        break

print("\nFinal Inventory")
print(inventory)