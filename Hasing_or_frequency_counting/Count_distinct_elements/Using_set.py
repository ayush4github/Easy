arr = list(map(int, input("Enter elements of array separated by space: ").split()))
count = len(set(arr))
print("Count of distinct elements is: ", count)