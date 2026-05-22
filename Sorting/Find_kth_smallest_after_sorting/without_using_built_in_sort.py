def find_smallest_kth_element_without_using_built_in_sort(numbers, k):
    length = len(numbers)
    for outer_index in range(length):
        for inner_index in range(outer_index+1, length):
            if numbers[outer_index]>numbers[inner_index]:
                numbers[outer_index], numbers[inner_index]=numbers[inner_index], numbers[outer_index]
    return numbers[k-1]
numbers = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter value of k for kth smallest element: "))
result = find_smallest_kth_element_without_using_built_in_sort(numbers, k)
print("Smallest kth element in array of numbers is: ", result)