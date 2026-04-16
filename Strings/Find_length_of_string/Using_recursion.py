def string_length(s, index =0):
    if index == len(s):
        return 0
    return 1 + string_length(s, index + 1)