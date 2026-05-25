def power_of(base, exponent):
    if exponent == 0:
        return 1
    return base * power_of(base, exponent-1)
base = int(input("Enter the base to find power of: "))
exponent = int(input("Enter the exponent to find power: "))
result = power_of(base, exponent)
print("Answer ", result)