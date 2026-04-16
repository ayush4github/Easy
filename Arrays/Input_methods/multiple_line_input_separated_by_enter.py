try:
    n = int(input())
    arr = []
    for i in range(n):
        element = int(input())
        arr.append(element)
except:
    print("Invalid input")
print(arr)