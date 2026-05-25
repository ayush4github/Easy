def reverse_array(array):
    #Base case
    if len(array) == 0:
        return []
    #Recursive formula
    return [array[-1]] + reverse_array(array[:-1])
#Input
array = list(map(int, input("Enter elements of array separated by space: ").split()))
#Output
print("Reverse array: ", reverse_array(array))