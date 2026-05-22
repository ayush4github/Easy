def find_kth_smallest_after_sorting(numbers, k):
    sorted_numbers = sorted(numbers)
    # kth smallest number will be at [k-1]th index after sorting
    result = sorted_numbers[k-1]
    return result
numbers = list(map(int, input("Enter numbers of array separaed by space: ").split()))
k = int(input("Enter the value of k to find kth smallest element: "))
kth_smallest_element = find_kth_smallest_after_sorting(numbers, k)
print("The kth smamlest number after sorting is: ", kth_smallest_element)
