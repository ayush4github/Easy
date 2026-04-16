Expression = input("Enter your string here: ")
sign = 1
stack = [1]
result = ""
i = 0
while i < len(Expression):
    if Expression[i] == "+":
        sign = stack[-1]
    elif Expression[i] == "-":
        sign = -stack[-1]
    elif Expression[i] == "(":
        stack.append(sign)
    elif Expression[i] == ")":
        stack.pop()
    else:
        if Expression[i].isalpha():
            if sign ==1:
                result = result + "+" + Expression[i]
            else:
                result = result + "-" + Expression[i]
    i = i +1
print(result.lstrip("+"))