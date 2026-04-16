def reverse_stack(s):
    stack = list(s)
    result = ""
    while stack:
        result = result + stack.pop()
    return result
s = input()
print(reverse_stack(s))