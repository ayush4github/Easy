arr = list(map(int, input().split()))
if len(arr) == 0:
    print("Empty array")
largest_element = float('-inf')
for element in arr:
    if element > largest_element:
        largest_element = element
print(largest_element)