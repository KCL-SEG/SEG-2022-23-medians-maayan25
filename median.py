"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()

numSize = len(numbers)
median = 0
if numSize % 2 == 1:
    median = numbers[numSize//2]
else:
    total = numbers[numSize//2-1] + numbers[numSize//2]
    median = total/2

print(median)
