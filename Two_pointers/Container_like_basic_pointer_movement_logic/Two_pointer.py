def max_container_area(heights):
    left_pointer = 0
    right_pointer = len(heights)-1
    max_area = 0
    while left_pointer<right_pointer:
        height = min(heights[left_pointer], heights[right_pointer])
        width = right_pointer - left_pointer
        area =height*width
        if area>max_area:
            max_area=area
            best_left_height = heights[left_pointer]
            best_right_height = heights[right_pointer]
        if heights[left_pointer]<heights[right_pointer]:
            left_pointer+=1
        else:
            right_pointer-=1
    return max_area, best_left_height, best_right_height
heights = list(map(int, input("Enter heights separated by space: ").split()))
Maximum_area = max_container_area(heights)
print("Maximum area is: ", Maximum_area)