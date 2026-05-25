def reverse_string(string, left_index, right_index):
    if left_index >= right_index:
        return
    string[left_index], string[right_index] = string[right_index], string[left_index]
    reverse_string(string, left_index+1, right_index-1)
text = input("Enter a string: ")
string = list(text)
reverse_string(string, 0, len(string)-1)
result = "".join(string)
print("Reversed string: ", result)