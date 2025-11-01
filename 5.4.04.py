data = [10, "world", 0, -5, 20, True, [], 3.5]

total = 0

for value in data:
    if type(value) == int or type(value) == float:
        total += value

print(total)