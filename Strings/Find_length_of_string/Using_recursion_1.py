def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])
s = input().strip()
print(string_length(s))