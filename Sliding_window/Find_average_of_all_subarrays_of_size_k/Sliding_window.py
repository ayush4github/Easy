def find_average_subarray_k(array, k):
    result = []
    window_sum=0
    for right_pointer in range(len(array)):
        window_sum+=array[right_pointer]
        if right_pointer>=k-1:
            average=window_sum/k
            result.append(average)
            window_sum-=array[right_pointer-k+1]
    return result
n = int(input("Enter number of elements in array: "))
array = []
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
k = int(input("Enter window size: "))
Result = find_average_subarray_k(array, k)
print("Result is: ", Result)