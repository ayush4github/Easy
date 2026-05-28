def decimal_to_binary(number):
    #Base case
    if number == 0:
        return
    #Recursive call
    decimal_to_binary(number //2)
    #Print remainder
    print(number % 2, end = "")
#Input
number = int(input("Enter a decimal number: "))
#Special case for 0
if number == 0:
    print("Binary = 0")
else:
    print("Binary = ", end = " ")
    decimal_to_binary(number)