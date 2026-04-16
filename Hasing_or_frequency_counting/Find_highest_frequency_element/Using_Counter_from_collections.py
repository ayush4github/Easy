from collections import Counter
Array = list(map(int, input("Enter elements of array separated by space here: ").split()))
freq=Counter(Array)
result = freq.most_common(1)[0][0]
print("Highest frequency element: ", result)