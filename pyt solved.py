print("Number Pyramid")
rows = int(input("Enter rows: "))
i = 1
total = 0

while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        total = total + j
        j = j + 1
    print()  # Moves to the next line after each row
    i = i + 1

print("Total sum:", total)

# Added missing colon and fixed indentation
if total > 100:
    print("Large pyramid")
else:
    print("Small pyramid")

# Added missing closing parenthesis
average = total / rows
print("Average:", average)