d1 = {"яблоки": 10, "груши": 5, "бананы": 3}
d2 = {"груши": 7, "бананы": 4, "апельсины": 8}

merged = d1.copy()

for key, value in d2.items():
    merged[key] = merged.setdefault(key, 0) + value

print(merged)