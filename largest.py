def find_largest_number(numbers):
    if not numbers:
        return None  # Handle empty list case
    
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print (find_largest_number([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 9