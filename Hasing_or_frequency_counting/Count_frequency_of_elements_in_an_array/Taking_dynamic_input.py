Array = input("Enter your array here: ")
def parse_input(user_input):
    try:
        return [int(x) for x in user_input.split()]
    except ValueError:
        return user_input.split()
arr = parse_input(Array)
if not arr:
    print({})
else:
    freq = {}
    for element in arr:
        freq[element] =freq.get(element, 0)+1
    print(freq)