def invert_dict(d):
    invert_dict = {}
    for key, value in d.items():
        invert_dict[value] = key
    return invert_dict

print(invert_dict({"a":1, "b":2}))