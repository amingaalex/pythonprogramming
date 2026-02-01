# Example: Working with operators, conditions, and loops

# Arithmetic operators
x = 6
y = 2
print("x ** y =", x ** y)   # Exponentiation
print("x // y =", x // y)   # Floor division
print("x % y =", x % y)     # Modulus

# Assignment operator
z = 10
z += 5   # same as z = z + 5
print("z after += 5:", z)

# Logical operators
a = True
b = False
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)

# Bitwise operators
m = 4   # 0100 in binary
n = 11  # 1011 in binary
print("m | n =", m | n)   # Bitwise OR
print("m & n =", m & n)   # Bitwise AND
print("m >> 2 =", m >> 2) # Right shift

# Conditional statement
if (x ** 2 > 20 and y < 10):
    print("Condition met: x squared is greater than 20 and y is less than 10")

# Loop with operator usage
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)   # exponentiation inside loop
print("Squares:", squares)
