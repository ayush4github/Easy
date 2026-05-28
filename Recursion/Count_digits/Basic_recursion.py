def count_digits(number):
    #Base case
    if number == 0:
        return 0
    #Recursive Formula
    return 1 + count_digits(number//10)
#Input
number = int(input("Enter a number: "))
#Handling zero separately
if number == 0:
    print("Number of digits = 1")
else:
    result = count_digits(abs(number))
    print("Number of digits: ", result)