def fibonacci(number):
    #Base case
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number -1) + fibonacci(number-2)
terms = int(input("Enter number of terms: "))
for current_number in range(terms):
    print(fibonacci(current_number), end = " ")