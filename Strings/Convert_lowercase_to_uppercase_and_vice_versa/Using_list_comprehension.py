String = input()
converted = "".join(
    ch.upper() if ch.islower()
    else ch.lower() if ch.isupper()
    else ch
    for ch in String
)
print("Converted strings: ", converted)