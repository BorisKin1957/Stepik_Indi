letters = {"a": 10, "b": 20, "c": 25, "d": 15}

max_value = max(letters.values())

for letter, value in letters.items():
    if value == max_value:
        print(letter)
        break
