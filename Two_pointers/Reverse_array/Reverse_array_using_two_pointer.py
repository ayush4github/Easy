def reverse_array(array):
    left = 0
    right = len(array)-1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left = left +1
        right = right -1
    return array
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
reversed_array = reverse_array(arr)
print("Reversed array is: ", reversed_array)