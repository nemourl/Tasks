nums = [1, 4, 7, 2, 9, 8]

even_nums = []
odd_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
print(f"{even_nums}\n{odd_nums}")