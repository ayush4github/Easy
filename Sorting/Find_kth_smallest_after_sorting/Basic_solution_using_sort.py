def find_kth_smallest_after_sorting(numbers, k):
    numbers.sort()
    return numbers[k-1]
numbers = list(map(int, input("Enter numbers of the array separated by space: ").split()))
k = int(input("Enter the value of k to find the kth element from sorted array: "))
result = find_kth_smallest_after_sorting(numbers, k)
print("Kth smallest element after sorting the array is: ", result)