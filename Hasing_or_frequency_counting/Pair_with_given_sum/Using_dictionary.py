arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target = int(input("Enter the targeted sum here: "))
hashmap = {}
for element in arr:
    complement = target - element
    if complement in hashmap:
        result = [element, complement]
    hashmap[element] = True
print("Pair found: ", result)