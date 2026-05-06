arr = list(map(int, input("Enter elements of array separated by space: ").split()))
count = set()
for element in arr:
    count.add(element)
print("Count of distinct elements is: ", len(count))