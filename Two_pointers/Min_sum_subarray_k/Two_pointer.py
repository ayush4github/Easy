def min_sum_subarray(array, k):
    left_pointer = 0
    window_sum=0
    min_sum = float("inf")
    for right_pointer in range(len(array)):
        window_sum+=array[right_pointer]
        if right_pointer-left_pointer+1==k:
            min_sum = min(min_sum, window_sum)
            window_sum-=array[left_pointer]
            left_pointer+=1
    return min_sum
n = int(input("Enter number of elements in array: "))
array=[]
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
k = int(input("Enter size of subarray: "))
result = min_sum_subarray(array, k)
print("Minimum sum is: ", result)