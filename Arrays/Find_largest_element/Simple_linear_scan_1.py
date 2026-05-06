def largest_element():
    arr = list(map(int, input().split()))
    
    if len(arr) == 0:
        return None
    
    max_element = arr[0]
    
    for num in arr:
        if num > max_element:
            max_element = num
            
    return max_element


print(largest_element())