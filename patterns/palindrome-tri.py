n = 5

for i in range(1, n + 1):

    # Leading spaces
    print("  " * (n - i), end="")

    # Descending numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    # Ascending numbers
    for j in range(2, i + 1):
        print(j, end=" ")

    print()