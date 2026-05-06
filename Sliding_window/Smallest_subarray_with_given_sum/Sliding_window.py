def smallest_subarray_with_sum(array, target):
    left_pointer=0
    window_sum=0
    min_length=float("inf")
    for right_pointer in range(len(array)):
        window_sum+=array[right_pointer]
        while window_sum>=target:
            current_length=right_pointer-left_pointer+1
            min_length=min(min_length, current_length)
            window_sum-=array[left_pointer]
            left_pointer+=1
    return 0 if min_length==float('inf') else min_length