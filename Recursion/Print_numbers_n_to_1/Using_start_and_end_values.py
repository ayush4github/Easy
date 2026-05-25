def print_numbers_n_to_1(current, end):
    if current < end:
        return
    print(current)
    print_numbers_n_to_1(current-1, end)
current = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print_numbers_n_to_1(current, end)