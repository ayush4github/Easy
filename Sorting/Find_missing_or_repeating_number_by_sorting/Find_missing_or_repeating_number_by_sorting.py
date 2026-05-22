def find_missing_or_repeating_number_by_sorting(numbers):
    length = len(numbers)
    numbers.sort()
    missing_number = -1
    repeating_number = -1
    for index in range(length-1):
        if numbers[index]==numbers[index+1]:
            repeating_number = numbers[index]
        if numbers[index+1]-numbers[index]>1:
            missing_number = numbers[index]+1
    return missing_number, repeating_number
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
missing_number, repeating_number = find_missing_or_repeating_number_by_sorting(numbers)
print("Missing number: ", missing_number)
print("Repeating number: ", repeating_number)