def max_sum_subarray_k(array, k):
    left_pointer =0
    window_sum =0
    max_sum = float("-inf")
    for right_pointer in range(len(array)):
        window_sum+=array[right_pointer]
        if right_pointer-left_pointer+1==k:
            max_sum = max(max_sum, window_sum)
            window_sum-=array[left_pointer]
            left_pointer+=1
    return max_sum
n = int(input("Enter number of elements in array: "))
array =[]
for x in range(n):
    element = int(input("Enter elements of array: "))
    array.append(element)
k = int(input("Enter size of subarray: "))
Result = max_sum_subarray_k(array, k)
print("Maximum sum is: ", Result)