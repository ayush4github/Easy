def pair_with_sum(array, target):
    left_pointer = 0
    right_pointer = len(array)-1
    while left_pointer<right_pointer:
        current_sum = array[left_pointer]+array[right_pointer]
        if current_sum == target:
            return (array[left_pointer], array[right_pointer])
        elif current_sum < target:
            left_pointer +=1
        else:
            right_pointer-=1
    return None

array = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter targeted sum: "))
Pair_found = pair_with_sum(array, target)
print("Pair found: ", Pair_found)