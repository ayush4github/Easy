def print_numbers(current_number, end):
    if current_number > end:
        return
    print(current_number)
    print_numbers(current_number+1, end)
current_number = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print_numbers(current_number, end)