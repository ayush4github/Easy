def power_of(base, exponent):
    #Base case
    if exponent == 0:
        return 1
    #Recursive call
    half = power_of(base, exponent //2)
    #Even exponent
    if exponent % 2 ==0:
        return half * half
    #Odd exponent
    return base * half * half
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Answer: ", power_of(base, exponent))