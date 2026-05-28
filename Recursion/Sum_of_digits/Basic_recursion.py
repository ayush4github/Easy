def sum_of_digits(number):
    #Base case
    if number == 0:
        return 0
    #Last digit
    last_digit = number % 10
    #Remaining number
    remaining_number = number // 10
    #Recursion formula
    return last_digit + sum_of_digits(remaining_number)
#Input
number = int(input("Enter a number: "))
#Handle negative numbers
result = sum_of_digits(abs(number))
print("Sum of digits: ", result)