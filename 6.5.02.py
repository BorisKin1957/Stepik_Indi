
alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
    'w': 23, 'x': 24, 'y': 25, 'z': 26
}

words = input().split()

# Вычисляем вес каждого слова, суммируя веса букв
weight_of_words = [sum([alphabet[char.lower()] for char in word]) for word in words]

# Сортируем список слов и их весов в обратном порядке по весу и выводим слово с максимальным весом
print(sorted(zip(words[::-1], weight_of_words[::-1]), key=lambda x: x[1], reverse=True)[0][0])


