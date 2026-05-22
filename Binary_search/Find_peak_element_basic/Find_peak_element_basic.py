def find_peak_element(numbers):
    left_index = 0
    right_index = len(numbers)-1
    while left_index<right_index:
        middle_index = (left_index+right_index)//2
        if numbers[middle_index]<numbers[middle_index+1]:
            left_index = middle_index+1
        else:
            right_index = middle_index
    return left_index
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = find_peak_element(numbers)
print("Peak element index: ", result)
print("Peak element value: ", numbers[result])