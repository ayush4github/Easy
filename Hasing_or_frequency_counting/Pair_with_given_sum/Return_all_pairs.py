arr = list(map(int, input("Enter elements separated by space: ").split()))
target = int(input("Enter targeted sum: "))
seen = set()
pairs =set()
for element in arr:
    complement = target - element
    if complement in seen:
        pairs.add(tuple(sorted((element, complement))))
    seen.add(element)
print(list(pairs))