small = {"a": 1, "c": 3}
big = {"a": 1, "b": 2, "c": 3}

is_subset = small.items() <= big.items()

print(is_subset)