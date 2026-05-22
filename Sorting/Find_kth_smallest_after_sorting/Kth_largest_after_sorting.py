def find_kth_largest_number_after_sorting(numbers, k):
    numbers.sort()
    return numbers[-k]
numbers = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter the value of k to find kth largest element: "))
result = find_kth_largest_number_after_sorting(numbers, k)
print("Kth largest number after sorting is: ", result)