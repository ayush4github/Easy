def sum_of_first_n_natural_numbers(number):
    if number == 0:
        return 0
    return number + sum_of_first_n_natural_numbers(number-1)
n = int(input("Enter value of n: "))
result = sum_of_first_n_natural_numbers(n)
print("Sum of first n natural numbers is: ", result)