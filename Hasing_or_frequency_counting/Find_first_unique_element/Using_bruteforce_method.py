Array = list(map(int, input("Enter elements of array separated by space here: ").split()))
for i in range(len(Array)):
    if Array.count(Array[i])==1:
        print("First unique element: ", Array[i])
        break
else:
    print("No unique element found")