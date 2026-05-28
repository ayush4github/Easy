def product_of_digits(number):
    #Base case:
    if number == 0:
        return 1
    #Last digit
    last_digit = number % 10
    #Remaining number
    remaining_number = number // 10
    #Recursion formula
    return last_digit * product_of_digits(remaining_number)
#Input
number = int(input("Enter a number: "))
#Special handling for 0
if number == 0:
    print("Product of digits is: 0")
else:
    result = product_of_digits(number)
    print("Product of digits is: ", result)