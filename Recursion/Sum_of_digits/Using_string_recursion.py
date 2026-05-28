def sum_of_digits(number):
    #Base case
    if number == "":
        return 0
    #Recursive formula
    return int(number[0]) + sum_of_digits(number[1:])
#Input
number = input("Enter a number: ")
#Remove negative sign
if number[0] == "-":
    number = number[1:]
#Output
print("Sum of digits: ", sum_of_digits(number))