books = {
    'ASDFG': 320,
    'ZXC123': 250,
    'QWE': 110,
    'MNBVCXZ': 410,
    'LKH': 90
}

result = {}

for key, value in books.items():
    if not len(key) % 3:
        result.update({key: value})

print(result)