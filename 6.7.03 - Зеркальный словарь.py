
data = {'milk': 50, 'bread': 40, 'cheese': 50, 'butter': 70, 'eggs': 40}

tmp, result = {}, {}

for k, v in data.items():
    tmp.setdefault(v, []).append(k)

for k, v in tmp.items():
    result[k] = sorted(v)

print(result)