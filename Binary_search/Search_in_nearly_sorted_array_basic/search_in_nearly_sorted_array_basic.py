def search_nearly_sorted(numbers, target):
    left_index = 0
    right_index = len(numbers)-1
    while left_index <=right_index:
        middle_index = (left_index + right_index)//2
        if numbers[middle_index]==target:
            return middle_index
        if middle_index -1>=left_index and numbers[middle_index-1]==target:
            return middle_index -1
        if middle_index+1<=right_index and numbers[middle_index+1]==target:
            return middle_index+1
        if numbers[middle_index]<target:
            left_index = middle_index + 2
        else:
            right_index = middle_index - 2
    return -1
numbers = list(map(int, input("Enter nearly sorted numbers: ").split()))
target = int(input("Enter target: "))
result = search_nearly_sorted(numbers, target)
if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")