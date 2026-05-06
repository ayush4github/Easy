def find_average_subarray_k_v2(array, k):
    result = []
    window_sum=sum(array[:k])
    result.append(window_sum/k)
    for i in range(k, len(array)):
        window_sum+=array[i]
        window_sum-=array[i-k]
        result.append(window_sum/k)
    return result
n = int(input("enter number of elements in array: "))
array=[]
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
k = int(input("Enter window size: "))
Result = find_average_subarray_k_v2(array, k)
print("Result is: ", Result)