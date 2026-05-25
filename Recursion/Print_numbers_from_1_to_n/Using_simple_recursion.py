def print_numbers_from_1_to_n(number):
    if number == 0:
        return
    print_numbers_from_1_to_n(number-1)
    print(number)
number = int(input("Enter n: "))
print_numbers_from_1_to_n(number)