# Name: Alex Abere
# Admission Number: ADM BSCIT-05-0063/2024
# Exercise 1:palindrome checker

def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")  # normalize
    return s == s[::-1]

# Test
print(is_palindrome("Racecar"))  # True
print(is_palindrome("Python"))   # False
