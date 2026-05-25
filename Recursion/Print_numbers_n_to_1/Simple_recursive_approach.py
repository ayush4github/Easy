def print_numbers_n_to_1(number):
    if number == 0:
        return
    print(number)
    print_numbers_n_to_1(number-1)
number = int(input("Enter value of n: "))
print_numbers_n_to_1(number)