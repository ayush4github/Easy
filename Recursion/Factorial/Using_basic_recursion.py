def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)
number = int(input("Enter number to find factorial of: "))
result = factorial(number)
print("Factorial of the number ", number, " is: ", result)