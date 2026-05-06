def max_sum_subarray_k(array, k):
    if len(array)<k:
        return None
    window_sum = sum(array[:k])
    max_sum = window_sum
    for right_pointer in range(k, len(array)):
        window_sum+=array[right_pointer]
        window_sum-=array[right_pointer-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
n = int(input("Enter number of elements of array: "))
array = []
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
k = int(input("Enter length of subarray: "))
Maximum_sum = max_sum_subarray_k(array, k)
print("Maximum sum for subarray size ", k, "is", Maximum_sum)