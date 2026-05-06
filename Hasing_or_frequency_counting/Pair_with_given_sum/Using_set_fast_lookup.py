arr = list(map(int, input("Enter your array here: ").split()))
target = int(input("Enter the targeted sum: "))
seen = set()
for element in arr:
    complement = target - element
    if complement in seen:
        result = [complement, element]
    seen.add(element)
if result:
    print("Pair found: ", result)
else:
    print("No pair found")


