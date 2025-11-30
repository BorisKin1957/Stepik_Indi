scores = {
    'Иванов': 15,
    'Петров': 20,
    'Сидоров': 15,
    'Кузнецов': 25
}

result = {}

if scores:
    min_score = min(scores.values())
    for k, v in scores.items():
        if v > min_score:
            result[k] = v

print(result)