scores = {
    'Анна': (100, 1.0),
    'Ольга': (120, 0.8),
    'Геракл': (100, 1.2),
    'Игорь': (80, 1.5)
}
result = []
good_score = max(scores.values(), key=lambda x: x[0] * x[1])

for k, v in scores.items():
    if v[0] * v[1] == good_score[0] * good_score[1]:
        result.append(k)


print(result if len(result) > 1 else result[0])
