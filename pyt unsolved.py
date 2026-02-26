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
print()
i = i + 1
print("Total sum:", total)
if total > 100
print("Large pyramid")
else:
print("Small pyramid")
average = total / rows
print("Average:", average