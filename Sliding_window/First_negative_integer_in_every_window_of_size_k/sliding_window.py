from collections import deque
def first_negative_in_window(array, k):
    result = []
    negative_queue = deque()
    for right_pointer in range(len(array)):
        if array[right_pointer]<0:
            negative_queue.append(right_pointer)
        if negative_queue and negative_queue[0]<=right_pointer-k:
            negative_queue.popleft()
        if right_pointer>=k-1:
            if negative_queue:
                result.append(array[negative_queue[0]])
            else:
                result.append(0)
    return result
n = int(input("Enter number of elements in array: "))
array=[]
for x in range(n):
    element = int(input("Enter elements of array: "))
    array.append(element)
k = int(input("Enter window size: "))
Result = first_negative_in_window(array, k)
print("Result is: ", Result)