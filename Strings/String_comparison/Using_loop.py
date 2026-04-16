String = input("Enter your string here: ")
if not String:
    print("Invalid string")
result = ""
count = 1
for i in range(1, len(String)):
    if String[i] == String[i-1]:
        count = count+1
    else:
        result = result +  String[i-1] +str(count)
        count = 1
result = result + String[-1] + str(count)
print(result)