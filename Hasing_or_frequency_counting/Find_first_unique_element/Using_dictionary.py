Array = list(map(int, input("Enter elements of your array separated by space here: ").split()))
freq={}
for element in Array:
    freq[element] = freq.get(element, 0)+1
for element in Array:
    if freq[element] ==1:
        result = element
        print("First unique occuring element is: ", result)
        break
else:
    print("No unique occuring element found.")