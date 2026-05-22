def binary_search_basic(numbers, target):
    left_index = 0
    right_index = len(numbers)-1
    while left_index <=right_index:
        middle_index = (left_index + right_index)//2
        if numbers[middle_index]==target:
            return middle_index
        elif numbers[middle_index]<target:
            left_index = middle_index+1
        else:
            right_index = middle_index-1
    return -1
numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))
result = binary_search_basic(numbers, target)
if result !=-1:
    print("Element found at index", result)
else:
    print("Ëlement not found")