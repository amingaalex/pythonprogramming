# Name: Alex Abere
# Admission Number: ADM BSCIT-05-0063/2024
# Exercise 1:filter even numbers

def filter_even(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]

# Test
print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
