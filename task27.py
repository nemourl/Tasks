s = "программирование"

freq = {}

for char in s:
    freq[char] = freq.setdefault(char, 0) + 1

print(freq)