data = {"a": 1, "b": 2, "c": 3, "d": 4}
to_remove = ["b", "e", "c"]

for key in to_remove:
    data.pop(key, None)

print(data)