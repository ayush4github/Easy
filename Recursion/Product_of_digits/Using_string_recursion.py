def product_of_digits(number):
    #Base case
    if number == "":
        return 1
    #Recursive Formula
    return int(number[0]) * product_of_digits(number[1:])
#Input
number = input("Enter a number: ")
#Remove negative sign
if number == "-":
    number = number[1:]
#Special case for 0
if number == "0":
    print("Product of digits is: 0")
else:
    result = product_of_digits(number)
    print("Product of digits is: ", result)