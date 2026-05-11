def bubble_sort(numbers):
    length = len(numbers)
    for outer_index in range(length):
        for inner_index in range(0, length-outer_index-1):
            if numbers[inner_index]>numbers[inner_index+1]:
                numbers[inner_index], numbers[inner_index+1]=numbers[inner_index+1], numbers[inner_index]
    return numbers
numbers = list(map(int, input("Enter numbers to sort separated by space: ").split()))
result = bubble_sort(numbers)
print("Sorted list is: ", result)
