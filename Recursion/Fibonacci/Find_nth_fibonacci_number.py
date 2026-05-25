def nth_fibonacci_number(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    # Recursive formula
    return nth_fibonacci_number(number-1) + nth_fibonacci_number(number-2)
number = int(input("Enter n: "))
result = nth_fibonacci_number(number)
print("nth Fibonacci number: ", result)