String = input("Enter your string here: ")
i = 0
result = ""
while i < len(String):
    count = 1
    while i + 1 < len(String) and String[i] == String[i+1]:
        i = i +1
        count = count + 1
    result = result + String[i] + str(count)
    i = i+1
print(result)