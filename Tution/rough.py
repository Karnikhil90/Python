num = 5 * 2
for i in range(1, num + 1, 2):
    for k in range(1, num + 1 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Modified loop to ensure equal number of stars in the last row
for i in range(num - 2, 0, -2):
    for k in range(num - i, 0, -1):
        print(" ", end="")
    for j in range(1, i + 2):  # Adjusted to add 1 more star
        print("*", end=" ")
    print()
