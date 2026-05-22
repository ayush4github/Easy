def find_duplicates_using_sort(numbers):
    numbers.sort()
    duplicates = []
    length = len(numbers)
    for index in range(length-1):
        if numbers[index]==numbers[index+1]:
            if numbers[index] not in duplicates:
                duplicates.append(numbers[index])
    return duplicates
numbers = list(map(int, input("Enter numbers of the array separated by space: ").split()))
result = find_duplicates_using_sort(numbers)
print("Duplicates: ", result)