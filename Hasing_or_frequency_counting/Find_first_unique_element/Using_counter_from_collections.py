from collections import Counter
arr = list(map(int, input("Enter elements of array separated by space here: ").split()))
freq=Counter(arr)
for element in arr:
    if freq[element] ==1:
        print("First unique element: ", element)
        break
else:
    print("No unique element found")