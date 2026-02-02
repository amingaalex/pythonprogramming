# Name: Alex Abere
# Admission Number: ADM BSCIT-05-0063/2024
# Exercise 2: Names List Program

names = []

n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input("Enter name: ")
    names.append(name)

# Remove duplicates and sort alphabetically
unique_names = sorted(set(names))

print("\nSorted names without duplicates:")
for name in unique_names:
    print(name)

print("\nTotal number of names entered:", len(names))
